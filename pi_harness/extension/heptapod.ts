/**
 * heptapod pi extension: the physics tool chain inside the agent loop.
 *
 * The plain Claude Code arm of the ablation wrote a FeynRules file once and
 * was validated afterwards by the harness. This extension gives the agent the
 * same validator the harness scores with, so it can write, check and repair
 * before it hands anything in:
 *
 *   lint_model      deterministic lints (fr_lint.py), milliseconds
 *   validate_model  FeynRules compile + 4 consistency checks + MadGraph import
 *   massbasis       symbolic tadpoles / mass matrix / inverted couplings (sympy)
 *   review_model    an independent reviewer (child pi, fresh context) that
 *                   compares model.fr with the paper, so passing the chain by
 *                   deleting physics does not go unnoticed
 *
 * Guards: every file tool is confined to the sandbox (HEPTAPOD_SANDBOX), and
 * bash is refused. The runner enables only read/write/edit/grep/find/ls plus
 * these tools, but the guard holds even if a flag is wrong.
 *
 * Environment (set by run_pi.py):
 *   HEPTAPOD_SANDBOX   sandbox root; the only readable/writable tree
 *   HEPTAPOD_RUNDIR    where validation outputs and tool_calls.jsonl go
 *   HEPTAPOD_HEPVAL    path to hepval.py
 *   HEPTAPOD_PYTHON    python interpreter (default python3)
 *   HEPTAPOD_ROLE      "agent" (all tools) or "reviewer" (guard only)
 *   HEPTAPOD_VALIDATE_BUDGET, HEPTAPOD_REVIEW_BUDGET   calls allowed per run
 *   HEPTAPOD_PI        pi binary for the reviewer (default pi)
 *   HEPTAPOD_MODEL     the agent's model
 *   HEPTAPOD_REVIEW_MODEL   model for the reviewer (default: HEPTAPOD_MODEL)
 *   HEPTAPOD_REVIEW_EXTRA_EXT   extra extensions for the reviewer, comma-separated (tests)
 */

import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { Type } from "typebox";
import { spawn } from "node:child_process";
import { appendFileSync, mkdirSync, readFileSync, realpathSync, writeFileSync, existsSync } from "node:fs";
import { dirname, isAbsolute, join, relative, resolve } from "node:path";

const env = process.env;
const SANDBOX = env.HEPTAPOD_SANDBOX ? realpathSync(env.HEPTAPOD_SANDBOX) : "";
const RUNDIR = env.HEPTAPOD_RUNDIR ?? "";
const HEPVAL = env.HEPTAPOD_HEPVAL ?? "";
const PYTHON = env.HEPTAPOD_PYTHON ?? "python3";
const ROLE = env.HEPTAPOD_ROLE ?? "agent";
const VALIDATE_BUDGET = Number(env.HEPTAPOD_VALIDATE_BUDGET ?? "6");
const REVIEW_BUDGET = Number(env.HEPTAPOD_REVIEW_BUDGET ?? "2");

const FILE_TOOLS = new Set(["read", "write", "edit", "grep", "find", "ls"]);

function log(rec: Record<string, unknown>) {
	if (!RUNDIR) return;
	mkdirSync(RUNDIR, { recursive: true });
	const file = ROLE === "reviewer" ? "reviewer_tool_calls.jsonl" : "tool_calls.jsonl";
	appendFileSync(join(RUNDIR, file), JSON.stringify({ t: Date.now() / 1000, role: ROLE, ...rec }) + "\n");
}

/** Resolve a tool path the way the built-in tools do, then require it to sit in the sandbox. */
function insideSandbox(p: string, cwd: string): { ok: boolean; abs: string } {
	const clean = p.startsWith("@") ? p.slice(1) : p;
	const abs = resolve(isAbsolute(clean) ? clean : join(cwd, clean));
	let real = abs;
	try {
		real = realpathSync(abs);
	} catch {
		// A new file: check its directory instead.
		try {
			real = join(realpathSync(dirname(abs)), abs.slice(dirname(abs).length + 1));
		} catch {
			real = abs;
		}
	}
	const rel = relative(SANDBOX, real);
	return { ok: rel === "" || (!rel.startsWith("..") && !isAbsolute(rel)), abs: real };
}

function sandboxPath(p: string): string {
	const r = insideSandbox(p, SANDBOX);
	if (!r.ok) throw new Error(`path ${p} is outside the sandbox ${SANDBOX}`);
	return r.abs;
}

function run(cmd: string, args: string[], opts: { cwd?: string; env?: NodeJS.ProcessEnv; signal?: AbortSignal } = {}): Promise<{ code: number; out: string; err: string }> {
	return new Promise((res) => {
		const child = spawn(cmd, args, { cwd: opts.cwd, env: opts.env ?? env, stdio: ["pipe", "pipe", "pipe"] });
		let out = "";
		let err = "";
		child.stdout.on("data", (d) => (out += d));
		child.stderr.on("data", (d) => (err += d));
		const kill = () => child.kill("SIGTERM");
		opts.signal?.addEventListener("abort", kill, { once: true });
		child.on("close", (code) => {
			opts.signal?.removeEventListener("abort", kill);
			res({ code: code ?? -1, out, err });
		});
		child.stdin.end();
	});
}

const text = (t: string) => ({ content: [{ type: "text" as const, text: t }], details: {} });

const REVIEW_PROMPT = `You are an independent referee. You did not write the model under review.

Files in the working directory: the paper (LaTeX source under eval/benchmark_runs/*/text/),
SM.fr (the Standard Model file the add-on is loaded on top of), and the model under review, MODEL_PATH.

Read the paper's model-defining sections and the whole model file. Report every place where the
model does not implement the paper's model. Check, term by term:
- every new field of the paper is present, with the paper's spin, colour/SU(2) representation,
  hypercharge/charge and any new U(1) charge;
- every Lagrangian term of the paper is present with the paper's coefficient, sign,
  normalisation (fractions, roots, 1/Lambda powers) and index/chirality structure;
- nothing the paper has was dropped or set to zero, and nothing was added that the paper does not have
  (kinetic and mass terms for new fields, SM-override bookkeeping such as LSM - LHiggs, and
  mixing-angle reparametrisations that are equivalent to the paper's are fine);
- mixing: the mass eigenstates and the angle match the paper's definitions.

Do not comment on FeynRules syntax or style. Output a numbered list of discrepancies, each with the
paper equation or LaTeX line and the model line, and a severity (physics-changing / cosmetic).
If you find none, say "NO DISCREPANCIES".`;

export default function (pi: ExtensionAPI) {
	pi.on("tool_call", async (event, ctx) => {
		if (!SANDBOX) return undefined;
		if (event.toolName === "bash") {
			log({ event: "blocked", tool: "bash", input: event.input });
			return { block: true, reason: "bash is not available in this harness; use the file tools and the heptapod tools" };
		}
		if (FILE_TOOLS.has(event.toolName)) {
			const p = (event.input as { path?: string }).path ?? ".";
			const r = insideSandbox(p, ctx.cwd);
			if (!r.ok || /reference_cache/.test(r.abs)) {
				log({ event: "blocked", tool: event.toolName, path: p });
				return { block: true, reason: `path ${p} is outside the sandbox; only files under ${SANDBOX} exist for this task` };
			}
		}
		log({ event: "call", tool: event.toolName, input: event.input });
		return undefined;
	});

	if (ROLE === "reviewer") return;

	let validations = 0;
	let reviews = 0;

	pi.registerTool({
		name: "lint_model",
		label: "Lint model",
		description:
			"Deterministic lints for a FeynRules add-on .fr file (milliseconds). Each finding names the rule and the stage it predicts: compile, checks, mg5, harness or warn. Run it after every edit, before validate_model.",
		promptSnippet: "lint_model: fast deterministic lints of a .fr file",
		parameters: Type.Object({ path: Type.String({ description: "the .fr file, e.g. model.fr" }) }),
		async execute(_id, params, signal) {
			const fr = sandboxPath(params.path);
			const r = await run(PYTHON, [HEPVAL, "lint", fr], { signal });
			log({ event: "result", tool: "lint_model", code: r.code });
			if (r.code !== 0) throw new Error(r.err.slice(-2000) || "lint failed");
			return text(r.out);
		},
	});

	pi.registerTool({
		name: "validate_model",
		label: "Validate model",
		description:
			`Run the real validation chain on a .fr file: FeynRules compile (Wolfram), the four FeynRules consistency checks (hermiticity, kinetic_diagonal, mass_diagonal, mass_spectrum), then MadGraph 'import model'. This is the exact chain the benchmark scores. Takes 1 to 10 minutes; calls queue for one kernel. Budget: ${VALIDATE_BUDGET} calls per run. Returns the verdicts, FeynRules' explanation for each failed check (including the offending non-diagonal terms), and the distinct lines of the compile log.`,
		promptSnippet: "validate_model: FeynRules compile + 4 checks + MadGraph import (the scored chain; budgeted)",
		parameters: Type.Object({ path: Type.String({ description: "the .fr file, e.g. model.fr" }) }),
		async execute(_id, params, signal, onUpdate) {
			const fr = sandboxPath(params.path);
			if (validations >= VALIDATE_BUDGET) {
				log({ event: "budget", tool: "validate_model" });
				throw new Error(`validation budget exhausted (${VALIDATE_BUDGET} calls). Use lint_model and massbasis, fix what the last report named, and finish.`);
			}
			validations += 1;
			onUpdate?.({ content: [{ type: "text", text: `validation ${validations}/${VALIDATE_BUDGET} running (queued for the Wolfram kernel if another run holds it)...` }], details: {} });
			const lint = await run(PYTHON, [HEPVAL, "lint", fr], { signal });
			const r = await run(PYTHON, [HEPVAL, "validate", fr, "--out", join(RUNDIR, "validation")], { signal });
			log({ event: "result", tool: "validate_model", n: validations, code: r.code, head: r.out.slice(0, 600) });
			if (r.code !== 0) throw new Error(`validator error (not a model verdict): ${r.err.slice(-1500)}`);
			const report = `validation ${validations}/${VALIDATE_BUDGET} (this report is saved as validation/call${validations}.md)\n\n${r.out}\n\n## lint findings\n${lint.out}`;
			mkdirSync(join(SANDBOX, "validation"), { recursive: true });
			writeFileSync(join(SANDBOX, "validation", `call${validations}.md`), report);
			return text(report);
		},
	});

	pi.registerTool({
		name: "massbasis",
		label: "Mass basis",
		description: `Symbolic quadratic-sector analysis of a scalar potential (sympy, about 1 s). Give the potential V (the Lagrangian contains -V) in gauge-basis symbols, the substitutions that express each gauge-basis field through the vev and the mass-basis REAL fields (split complex fields into real components), the mixing angles as sine/cosine symbol pairs, the target physical masses, and the parameters to solve for. Returns the tadpoles, the mass-squared matrix at the vacuum, which off-diagonal entries are non-zero, and with solve_for the inverted parametrisation (couplings as functions of physical masses and angles) in Mathematica syntax, verified: tadpoles zero, off-diagonals zero, diagonals equal to the target masses squared. Use it for h-S, Z-Z' or any scalar mixing BEFORE writing the Internal parameters, so CheckDiagonalMassTerms can pass. Example spec: {"potential": "-muPsq/2*p**2 + lambdaP/8*p**4 - muSsq/2*s**2 + lambdaS/8*s**4 + lambdaPS/4*p**2*s**2", "substitutions": {"p": "vev + ct*H + st*h2", "s": "vs - st*H + ct*h2"}, "fields": ["H", "h2"], "angles": {"theta": ["st", "ct"]}, "targets": {"H": "MH", "h2": "Mh2"}, "solve_for": ["muPsq", "muSsq", "lambdaP", "lambdaS", "lambdaPS"]}`,
		promptSnippet: "massbasis: tadpoles, mass matrix and inverted couplings for scalar mixing (sympy)",
		parameters: Type.Object({
			spec: Type.String({ description: "JSON object with potential, substitutions, fields, angles, targets, solve_for" }),
		}),
		async execute(_id, params, signal) {
			try {
				JSON.parse(params.spec);
			} catch (e) {
				throw new Error(`spec is not valid JSON: ${(e as Error).message}`);
			}
			const r = await run(PYTHON, [HEPVAL, "massbasis", params.spec], { signal });
			log({ event: "result", tool: "massbasis", code: r.code });
			if (r.code !== 0) throw new Error(r.err.slice(-2000));
			return text(r.out);
		},
	});

	pi.registerTool({
		name: "review_model",
		label: "Independent review",
		description: `An independent referee (a fresh agent that did not write the model) reads the paper and the .fr file and lists every place the model departs from the paper: missing or extra fields and terms, wrong coefficients, signs, normalisations, charges, mixing. Run it once the chain passes (or when you are unsure a fix preserved the physics). Budget: ${REVIEW_BUDGET} calls per run. A physics-changing discrepancy must be fixed even if the chain passes.`,
		promptSnippet: "review_model: independent paper-vs-model referee (budgeted)",
		parameters: Type.Object({ path: Type.String({ description: "the .fr file, e.g. model.fr" }) }),
		async execute(_id, params, signal, onUpdate) {
			const fr = sandboxPath(params.path);
			if (reviews >= REVIEW_BUDGET) throw new Error(`review budget exhausted (${REVIEW_BUDGET} calls)`);
			reviews += 1;
			onUpdate?.({ content: [{ type: "text", text: `review ${reviews}/${REVIEW_BUDGET} running...` }], details: {} });
			const rel = relative(SANDBOX, fr);
			// The referee sees a frozen copy, so the author cannot edit the file mid-review.
			const snap = join(SANDBOX, "validation", `review${reviews}_${rel.replace(/\//g, "_")}`);
			mkdirSync(dirname(snap), { recursive: true });
			writeFileSync(snap, readFileSync(fr));
			const args = [
				"-p", "--no-session", "--no-context-files", "--no-skills", "--no-prompt-templates", "--no-extensions",
				"-e", new URL(import.meta.url).pathname,
				// Tests load a scripted provider into the referee too.
				...(env.HEPTAPOD_REVIEW_EXTRA_EXT ?? "").split(",").filter(Boolean).flatMap((p) => ["-e", p]),
				"--tools", "read,grep,find,ls",
				...(env.HEPTAPOD_REVIEW_MODEL ? ["--model", env.HEPTAPOD_REVIEW_MODEL] : env.HEPTAPOD_MODEL ? ["--model", env.HEPTAPOD_MODEL] : []),
				REVIEW_PROMPT.replace("MODEL_PATH", relative(SANDBOX, snap)),
			];
			const r = await run(env.HEPTAPOD_PI ?? "pi", args, {
				cwd: SANDBOX,
				env: { ...env, HEPTAPOD_ROLE: "reviewer" },
				signal,
			});
			log({ event: "result", tool: "review_model", n: reviews, code: r.code, head: r.out.slice(0, 400) });
			if (r.code !== 0) throw new Error(`reviewer failed: ${r.err.slice(-1500)}`);
			writeFileSync(snap.replace(/\.fr$/, "") + ".review.md", r.out);
			return text(`review ${reviews}/${REVIEW_BUDGET} of ${rel}\n\n${r.out}`);
		},
	});

	pi.on("agent_end", async () => {
		log({ event: "agent_end", validations, reviews, model_exists: existsSync(join(SANDBOX, "model.fr")) });
	});
}
