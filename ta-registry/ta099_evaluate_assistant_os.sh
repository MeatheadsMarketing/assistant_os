#!/bin/bash
# TA-099: Meta-Assistant Evaluator
# Scans all assistants in the registry and produces a system health report

REGISTRY="./ta-registry"
REPORT="$REGISTRY/meta_scorecard.md"

echo "# Assistant OS Health Report" > "$REPORT"
echo "" >> "$REPORT"
echo "| TA ID | Name | Status |" >> "$REPORT"
echo "|-------|------|--------|" >> "$REPORT"

for dir in $(find "$REGISTRY" -maxdepth 1 -type d -name 'TA-*' | sort); do
  TA_ID=$(basename "$dir")
  CONFIG="$dir/config.json"
  STATUS="missing"

  if [[ -f "$CONFIG" ]]; then
    NAME=$(jq -r .Name "$CONFIG")
    CLI=$(jq -r .CLI_File "$CONFIG")
    if [[ -f "$dir/$CLI" ]]; then
      STATUS="✅ built"
    else
      STATUS="🚧 config only"
    fi
    echo "| $TA_ID | $NAME | $STATUS |" >> "$REPORT"
  fi
done

echo "✅ Meta-assistant report generated: $REPORT"
