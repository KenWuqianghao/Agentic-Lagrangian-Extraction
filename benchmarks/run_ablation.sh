#!/usr/bin/env bash
# Rerun the extraction benchmark with the v3 prompt and compare three arms:
#
#   v3_tools     Read/Grep/Glob + schema + renderer, LaTeX paper source
#   v3_notools   no tools at all, paper + SM.fr inlined, agent writes the .fr
#   v3txt_tools  as v3_tools but with the PDF-extracted text (isolates the
#                effect of the paper source; skip with ARMS="tools notools")
#
# then score every arm against the FeynRules-DB references and write the
# side-by-side report. Resumable: re-running skips agents that already
# produced output and validations that already passed.
#
# Needs: a logged-in `claude` CLI (`claude auth status` -> loggedIn true),
# an activated Wolfram Engine, FeynRules and MadGraph (config.py).
#
#   PAGES=EffLRSM,GeneralU1 SEEDS=2 eval/benchmark_runs/run_ablation.sh
#   PAGES=single eval/benchmark_runs/run_ablation.sh   # single-model papers + Ian's four
set -uo pipefail
cd "$(dirname "$0")/../.."
PY=.venv/bin/python
BR=eval/benchmark_runs

IAN4="Top-Philic-Zprime,368sextets,EffLRSM,GeneralU1"
PAGES="${PAGES:-$IAN4}"
if [ "$PAGES" = "single" ]; then
  PAGES="$($PY - <<'EOF'
import json
sel = json.load(open("eval/benchmark_runs/single_model_papers.json"))
pages = [r["page"] for r in sel["rows"] if r["single_model"]]
for p in "Top-Philic-Zprime,368sextets,EffLRSM,GeneralU1".split(","):
    if p not in pages:
        pages.append(p)
print(",".join(pages))
EOF
)"
fi
SEEDS="${SEEDS:-2}"
ARMS="${ARMS:-tools notools txt}"
PARALLEL="${PARALLEL:-4}"
export RERUN_AGENT_MODEL="${RERUN_AGENT_MODEL:-claude-opus-5}"
export VBENCH_COMPILE_TIMEOUT="${VBENCH_COMPILE_TIMEOUT:-1800}"
export RERUN_OUT="${RERUN_OUT:-/tmp/rerun_bench}"
ADD="$BR/prompt_addendum_v3.txt"

if ! claude auth status 2>/dev/null | grep -q '"loggedIn": true'; then
  cat >&2 <<'MSG'
The headless `claude` CLI is not logged in, so this script cannot run the agent
stage. Two ways forward:

  1. Run `claude login` in a terminal, then re-run this script.
  2. Drive the agent stage from an interactive Claude Code session instead:

       python eval/benchmark_runs/subagent_bench.py prepare --pages <pages> \
           --variant v3_tools --engine-mode tools --paper-source tex \
           --addendum eval/benchmark_runs/prompt_addendum_v3.txt --seeds 2
       # run each manifest entry's user_prompt as a subagent, then
       python eval/benchmark_runs/subagent_bench.py ingest --variant v3_tools \
           --workflow-dir <the session's subagent transcript directory>

     and re-run this script afterwards: the agent stage is skipped for runs
     that already have output, and only rendering, validation and scoring run.
MSG
  if [ "${ALLOW_NO_AGENT:-0}" != "1" ]; then exit 2; fi
  echo "[ablation] ALLOW_NO_AGENT=1: continuing with existing agent output only" >&2
fi

echo "[ablation] pages=$PAGES seeds=$SEEDS arms=$ARMS model=$RERUN_AGENT_MODEL"
VARIANTS=""
for arm in $ARMS; do
  case "$arm" in
    tools)   V=v3_tools;    MODE=tools;   SRC=tex ;;
    notools) V=v3_notools;  MODE=notools; SRC=tex ;;
    txt)     V=v3txt_tools; MODE=tools;   SRC=txt ;;
    *) echo "unknown arm $arm" >&2; exit 2 ;;
  esac
  VARIANTS="${VARIANTS:+$VARIANTS,}$V"
  echo "[ablation] === $V ($MODE / $SRC) ==="
  caffeinate -i $PY $BR/rerun_extract.py --pages "$PAGES" --variant "$V" \
    --engine-mode "$MODE" --paper-source "$SRC" --addendum "$ADD" \
    --seeds "$SEEDS" --parallel "$PARALLEL" --skip-existing --skip-validated
  $PY $BR/rerun_score.py --variant "$V" --seed 1 || true
done

$PY $BR/ablation_report.py --variants "v1,v2,$VARIANTS" --pages "$PAGES" --seeds "$SEEDS"
echo "[ablation] done: $BR/ablation_report.md"
