#!/bin/zsh
# Replay EffLRSM and SMWeinberg again (after replay.sh) into report_v2.md.
# usage: rereplay.sh [heptapod benchmark_runs dir]; PYTHON selects the interpreter.
OUT=${0:A:h}
REPO=${OUT:h:h}
H=${1:-$HOME/Documents/Github/heptapod/eval/benchmark_runs}
PY=${PYTHON:-python3}
failed=()
for p in EffLRSM SMWeinberg; do
  fr=$H/$p/rerun/pi_qwen_harness/s1/model/${p}_gen.fr
  mkdir -p $OUT/$p
  cp $fr $OUT/$p/model.fr || { echo "[replay] $p copy FAILED"; failed+=($p); continue; }
  echo "[replay] $p start $(date +%H:%M:%S)"
  $PY $REPO/pi_harness/hepval.py validate $fr --out $OUT/$p/validation --diag > $OUT/$p/report_v2.md 2> $OUT/$p/stderr.txt
  rc=$?
  echo "[replay] $p done $(date +%H:%M:%S) exit=$rc"
  (( rc )) && failed+=($p)
done
if (( ${#failed} )); then
  echo "[replay] FAILED: $failed"
  exit 1
fi
echo "[replay] RERUN DONE"
