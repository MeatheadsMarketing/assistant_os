
#!/bin/bash

ROOT=~/assistant-os-raycast

mkdir -p $ROOT/dashboards/phase1
mkdir -p $ROOT/dashboards/phase8
mkdir -p $ROOT/redteam/rounds
mkdir -p $ROOT/proof
mkdir -p $ROOT/ta-scripts
mkdir -p $ROOT/utilities
mkdir -p $ROOT/TA-Library

# Move dashboards safely with loops
for f in $ROOT/ta001_dashboard_v*.py; do [ -e "$f" ] && mv "$f" $ROOT/dashboards/phase1/; done
for f in $ROOT/ta002_dashboard_v*.py; do [ -e "$f" ] && mv "$f" $ROOT/dashboards/phase1/; done
for f in $ROOT/ta003_dashboard_v*.py; do [ -e "$f" ] && mv "$f" $ROOT/dashboards/phase1/; done

for f in $ROOT/ta004_dashboard_v*.py $ROOT/ta005_dashboard_v*.py $ROOT/ta006_dashboard_v*.py $ROOT/ta007_dashboard_v*.py \
         $ROOT/ta009_dashboard_v*.py $ROOT/ta012_dashboard_v*.py $ROOT/ta013_dashboard_v*.py $ROOT/ta014_dashboard_v*.py \
         $ROOT/ta020_dashboard_v*.py $ROOT/ta021_dashboard_v*.py $ROOT/ta022_dashboard_v*.py $ROOT/ta024_dashboard_v*.py \
         $ROOT/ta025_dashboard_v*.py $ROOT/ta027_dashboard_v*.py $ROOT/ta030_dashboard_v*.py $ROOT/ta045_dashboard_v*.py \
         $ROOT/ta048_dashboard_v*.py $ROOT/ta049_dashboard_v*.py $ROOT/ta050_dashboard_v*.py $ROOT/ta061_dashboard_v*.py \
         $ROOT/ta065_dashboard_v*.py $ROOT/ta069_dashboard_v*.py $ROOT/ta084_dashboard_v*.py $ROOT/ta094_dashboard_v*.py \
         $ROOT/ta100_dashboard_v*.py; do [ -e "$f" ] && mv "$f" $ROOT/dashboards/; done

for f in $ROOT/ta101_dashboard_v*.py $ROOT/ta102_dashboard_v*.py $ROOT/ta103_dashboard_v*.py $ROOT/ta104_dashboard_v*.py \
         $ROOT/ta105_dashboard_v*.py; do [ -e "$f" ] && mv "$f" $ROOT/dashboards/phase8/; done

# Move redteam files
for f in redteam_dashboard.py redteam_playbook.json redteam_summary_report.pdf; do
  [ -e $ROOT/$f ] && mv $ROOT/$f $ROOT/redteam/
done

[ -d $ROOT/proof_bundle/redteam_round_001 ] && mv $ROOT/proof_bundle/redteam_round_001 $ROOT/redteam/rounds/

# Move audit logs
for f in proof_bundle.zip input_trace_audit.md system_health_report.md drift_round_001_report.md redteam_summary_report.pdf; do
  [ -e $ROOT/$f ] && mv $ROOT/$f $ROOT/proof/
done

# Shell scripts
for f in $ROOT/*.sh; do [ -e "$f" ] && mv "$f" $ROOT/ta-scripts/; done

# Utility helpers
for f in ta_memory_updater.sh ta013_fact_extractor.sh add_instruction_version.sh; do
  [ -e $ROOT/$f ] && mv $ROOT/$f $ROOT/utilities/
done

# TA-Library
for f in $ROOT/TA-Library/*.csv; do [ -e "$f" ] && mv "$f" $ROOT/TA-Library/; done
[ -e $ROOT/ui_upgrades.json ] && mv $ROOT/ui_upgrades.json $ROOT/TA-Library/
for f in $ROOT/phase_evolution_matrix.*; do [ -e "$f" ] && mv "$f" $ROOT/TA-Library/; done
