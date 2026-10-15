#!/bin/zsh
# Replay the six pi Qwen near-miss models through the new in-loop validate (hepval --diag).
# usage: replay.sh [heptapod benchmark_runs dir]; PYTHON selects the interpreter.
OUT=${0:A:h}
REPO=${OUT:h:h}
H=${1:-$HOME/Documents/Github/heptapod/eval/benchmark_runs}
PY=${PYTHON:-python3}
failed=()
for p in B-L-SM HeavyN Wprime EffLRSM SMWeinberg pSPSS; do
  fr=$H/$p/rerun/pi_qwen_harness/s1/model/${p}_gen.fr
  mkdir -p $OUT/$p
  cp $fr $OUT/$p/model.fr || { echo "[replay] $p copy FAILED"; failed+=($p); continue; }
  echo "[replay] $p start $(date +%H:%M:%S)"
  $PY $REPO/pi_harness/hepval.py validate $fr --out $OUT/$p/validation --diag > $OUT/$p/report.md 2> $OUT/$p/stderr.txt
  rc=$?
  echo "[replay] $p done $(date +%H:%M:%S) exit=$rc"
  (( rc )) && failed+=($p)
done
if (( ${#failed} )); then
  echo "[replay] FAILED: $failed"
  exit 1
fi
echo "[replay] ALL DONE"
