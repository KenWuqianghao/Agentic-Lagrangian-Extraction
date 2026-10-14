#!/bin/zsh
# Replay EffLRSM and SMWeinberg again (after replay.sh) into report_v2.md.
H=$HOME/Documents/Github/heptapod/eval/benchmark_runs
OUT=$HOME/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay
for p in EffLRSM SMWeinberg; do
  fr=$H/$p/rerun/pi_qwen_harness/s1/model/${p}_gen.fr
  mkdir -p $OUT/$p
  cp $fr $OUT/$p/model.fr
  echo "[replay] $p start $(date +%H:%M:%S)"
  /opt/homebrew/bin/python3 $HOME/Documents/Github/Agentic-Lagrangian-Extraction/pi_harness/hepval.py validate $fr --out $OUT/$p/validation --diag > $OUT/$p/report_v2.md 2> $OUT/$p/stderr.txt
  rc=$?
  echo "[replay] $p done $(date +%H:%M:%S) exit=$rc"
done
echo "[replay] RERUN DONE"
