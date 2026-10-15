// opencode plugin for the open-model benchmark's toolkit2 arm.
//
// After every write, edit or patch that touches spec.json, run the toolkit
// (./frgen spec.json: schema check, renderer, lints) and append its report to
// that tool's result, so the agent sees the check whether or not it asks for
// it. In the first toolkit arm the check was a command the agent could skip,
// and Nemotron skipped it in 7 of 16 runs.
//
// Each run is logged to $FRGEN_HOOK_LOG (outside the sandbox) for the audit.

const EDIT_TOOLS = new Set(["write", "edit", "patch", "multiedit", "apply_patch"]);

export const FrgenHook = async ({ $, directory }) => {
  return {
    "tool.execute.after": async (input, output) => {
      if (!EDIT_TOOLS.has(input.tool)) return;
      if (!JSON.stringify(input.args ?? {}).includes("spec.json")) return;
      const report = await $`./frgen spec.json`.cwd(directory).nothrow().text();
      output.output =
        (output.output ?? "") +
        "\n\n[toolkit check, run automatically after this change to spec.json]\n" +
        report;
      const log = process.env.FRGEN_HOOK_LOG;
      if (log) {
        const line = JSON.stringify({ t: Date.now(), tool: input.tool, report: report.slice(0, 400) });
        const prev = (await Bun.file(log).exists()) ? await Bun.file(log).text() : "";
        await Bun.write(log, prev + line + "\n");
      }
    },
  };
};
