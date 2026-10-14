#!/bin/bash
# Does the gap change with a weaker model? Haiku 5.5, the shell arm (deck) against vanilla (Mac), 13 papers, one seed,
# the same conditions as the three-seed Sonnet comparison.
source ~/hep-tools/env.sh
cd /home/deck/code/ALE-ablation
export PI_HARNESS_RUNS=/home/deck/code/ALE-ablation/benchmarks/heptapod_ablation/runs
export HEPVAL_COMPILE_TIMEOUT=1350
L=$PI_HARNESS_RUNS/logs; M=${ALE_MAC_HOST:?set ALE_MAC_HOST to the ssh target of the Mac}
P13=331,ALRM_general,B-L-SM,EffLRSM,GeneralU1,HeavyN,MDMmodel,Monotops,SMWeinberg,Top-Philic-Zprime,Wprime,pNG,pSPSS
python cc_harness/run_cc.py run --arm shell --variant cc_haiku_shell --pages $P13 --model claude-haiku-5-5 \
  --validate-budget 10 --review-budget 2 --max-continuations 3 --parallel 2 >> $L/haiku_shell_run.log 2>&1
echo "haiku: shell agents done $(date '+%F %T')" >> $L/progress.txt
until [ "$(ssh -o BatchMode=yes -o ConnectTimeout=10 $M 'ls ~/ale-remote/runs/*/rerun/cc_haiku_vanilla/s1/run.json 2>/dev/null | wc -l' | tr -d ' ')" = 13 ]; do sleep 300; done
for p in ${P13//,/ }; do mkdir -p $PI_HARNESS_RUNS/$p/rerun/cc_haiku_vanilla && rsync -a $M:ale-remote/runs/$p/rerun/cc_haiku_vanilla/s1 $PI_HARNESS_RUNS/$p/rerun/cc_haiku_vanilla/; done
python cc_harness/run_cc.py score --variants cc_haiku_shell,cc_haiku_vanilla --pages $P13 >> $L/haiku_score.log 2>&1
echo "haiku scored $(date '+%F %T')" >> $L/progress.txt
