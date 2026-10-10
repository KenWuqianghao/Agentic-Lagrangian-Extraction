#!/bin/bash
# Three seeds per group under one set of conditions (4 h limit, two kernel slots, two agents per machine).
# Deck: the shell arm seeds 2 and 3, then vanilla seed 3. Mac (started separately): vanilla seed 2.
source ~/hep-tools/env.sh
cd /home/deck/code/ALE-ablation
export PI_HARNESS_RUNS=/home/deck/code/ALE-ablation/benchmarks/heptapod_ablation/runs
export HEPVAL_COMPILE_TIMEOUT=1350 VANILLA_AGENT_TIMEOUT=14400
L=$PI_HARNESS_RUNS/logs; M=kenwu@100.117.115.6
P13=331,ALRM_general,B-L-SM,EffLRSM,GeneralU1,HeavyN,MDMmodel,Monotops,SMWeinberg,Top-Philic-Zprime,Wprime,pNG,pSPSS
python cc_harness/run_cc.py run --arm shell --variant cc_sonnet_shell --pages $P13 --model claude-sonnet-5 \
  --validate-budget 10 --review-budget 2 --max-continuations 3 --parallel 2 --seeds 3 --first-seed 2 >> $L/seeds_shell_run.log 2>&1
echo "seeds: shell agents done $(date '+%F %T')" >> $L/progress.txt
python benchmarks/heptapod_ablation/run_vanilla.py run --variant cc_vanilla_fair --scorer-rules --pages $P13 --parallel 2 \
  --seeds 3 --first-seed 3 >> $L/seeds_vanilla_run.log 2>&1
echo "seeds: vanilla s3 agents done $(date '+%F %T')" >> $L/progress.txt
until [ "$(ssh -o BatchMode=yes -o ConnectTimeout=10 $M 'ls ~/ale-remote/runs/*/rerun/cc_vanilla_fair/s2/run.json 2>/dev/null | wc -l' | tr -d ' ')" = 13 ]; do sleep 300; done
for p in ${P13//,/ }; do mkdir -p $PI_HARNESS_RUNS/$p/rerun/cc_vanilla_fair && rsync -a $M:ale-remote/runs/$p/rerun/cc_vanilla_fair/s2 $PI_HARNESS_RUNS/$p/rerun/cc_vanilla_fair/; done
echo "seeds: mac vanilla s2 synced $(date '+%F %T')" >> $L/progress.txt
python cc_harness/run_cc.py score --variants cc_sonnet_shell,cc_vanilla_fair --pages $P13 --seeds 3 >> $L/seeds_score.log 2>&1
echo "seeds scored $(date '+%F %T')" >> $L/progress.txt
