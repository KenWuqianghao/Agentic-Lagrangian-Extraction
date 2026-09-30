#!/bin/zsh
# Replay the six pi Qwen near-miss models through the new in-loop validate (hepval --diag).
H=$HOME/Documents/Github/heptapod/eval/benchmark_runs
OUT=$HOME/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay
for p in B-L-SM HeavyN Wprime EffLRSM SMWeinberg pSPSS; do
  fr=$H/$p/rerun/pi_qwen_harness/s1/model/${p}_gen.fr
  mkdir -p $OUT/$p
  cp $fr $OUT/$p/model.fr
  echo "[replay] $p start $(date +%H:%M:%S)"
  /opt/homebrew/bin/python3 $HOME/Documents/Github/Agentic-Lagrangian-Extraction/pi_harness/hepval.py validate $fr --out $OUT/$p/validation --diag > $OUT/$p/report.md 2> $OUT/$p/stderr.txt
  echo "[replay] $p done $(date +%H:%M:%S) exit=$?"
done
echo "[replay] ALL DONE"
