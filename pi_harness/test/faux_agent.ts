/**
 * Scripted model for an offline end-to-end test of the harness plumbing.
 *
 * Registers provider "faux" (model "faux-1") whose replies are a fixed
 * script: the agent role reads the paper, tries to read outside the sandbox
 * (must be blocked), writes a known-good pNG model, lints it, runs massbasis,
 * validates it with the real chain, asks for a review, and stops. The
 * reviewer role reads one file and answers. The plain arm answers with one
 * fenced .fr block. No network, no credentials.
 *
 * FAUX_MODEL_FR: the .fr file the scripted agent writes.
 */

import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { readFileSync } from "node:fs";
import { createFauxCore, fauxAssistantMessage, fauxText, fauxToolCall } from "/Users/kenwu/.hermes/node/lib/node_modules/@earendil-works/pi-coding-agent/node_modules/@earendil-works/pi-ai/dist/providers/faux.js";

export default function (pi: ExtensionAPI) {
	const core = createFauxCore({ provider: "faux", models: [{ id: "faux-1", contextWindow: 400000, maxTokens: 16000 }] });
	const role = process.env.HEPTAPOD_ROLE ?? "agent";
	const plain = process.env.HEPTAPOD_ARM === "plain";
	const fr = readFileSync(process.env.FAUX_MODEL_FR ?? "", "utf8");
	const tool = (name: string, args: Record<string, unknown>) => fauxAssistantMessage([fauxToolCall(name, args)], { stopReason: "toolUse" });

	if (plain) {
		core.setResponses([fauxAssistantMessage([fauxText("Self-audit table omitted in the test.\n\n```mathematica\n" + fr + "\n```\n")])]);
	} else if (role === "reviewer") {
		core.setResponses([tool("read", { path: "SM.fr", limit: 3 }), fauxAssistantMessage("NO DISCREPANCIES (faux referee)")]);
	} else {
		const spec = JSON.stringify({
			potential: "-muPsq/2*p**2 + lambdaP/8*p**4 - muSsq/2*s**2 + lambdaS/8*s**4 + lambdaPS/4*p**2*s**2",
			substitutions: { p: "vev + ct*H + st*h2", s: "vs - st*H + ct*h2" },
			fields: ["H", "h2"], angles: { theta: ["st", "ct"] }, targets: { H: "MH", h2: "Mh2" },
			solve_for: ["muPsq", "muSsq", "lambdaP", "lambdaS", "lambdaPS"],
		});
		core.setResponses([
			tool("read", { path: "eval/benchmark_runs/pNG/text/1912.04008_source.tex", limit: 5 }),
			tool("read", { path: "/etc/hosts" }),
			tool("ls", { path: ".." }),
			tool("bash", { command: "ls /" }),
			tool("write", { path: "model.fr", content: fr }),
			tool("lint_model", { path: "model.fr" }),
			tool("massbasis", { spec }),
			tool("validate_model", { path: "model.fr" }),
			tool("review_model", { path: "model.fr" }),
			fauxAssistantMessage("Done: pNG model written; last validate_model verdict: see above."),
		]);
	}
	pi.registerProvider("faux", {
		baseUrl: "http://localhost.invalid",
		apiKey: "faux",
		api: core.api,
		models: [{ id: "faux-1", name: "faux", reasoning: false, input: ["text"], cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 }, contextWindow: 400000, maxTokens: 16000 }],
		streamSimple: core.streamSimple,
	});
}
