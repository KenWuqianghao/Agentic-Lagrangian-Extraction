#!/bin/bash
# A writable runs tree for the ablation: the stored tree
# (~/Documents/Github/heptapod/eval/benchmark_runs) is read-only, and run_cc.py
# reads its inputs (paper text, task prompt, prompt addendum) and writes its
# outputs under one root. This links the inputs and leaves rerun/ empty.
#
#   runs_root.sh [DIR]      default: runs/ next to this script (git-ignored)
#   export PI_HARNESS_RUNS=DIR
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
src="${ABLATION_STORED_RUNS:-$HOME/Documents/Github/heptapod/eval/benchmark_runs}"
dst="${1:-$here/runs}"
mkdir -p "$dst"
ln -sfn "$src/prompt_addendum_v3.txt" "$dst/prompt_addendum_v3.txt"
for page in 331 ALRM_general B-L-SM ChernSimonsPortal EffLRSM GeneralU1 HeavyN MDMmodel Monotops \
            NJLComposite SLQrules SMWeinberg Top-Philic-Zprime Wprime pNG pSPSS; do
  mkdir -p "$dst/$page/rerun"
  ln -sfn "$src/$page/text" "$dst/$page/text"
  ln -sfn "$src/$page/prompt.txt" "$dst/$page/prompt.txt"
done
echo "$dst"
