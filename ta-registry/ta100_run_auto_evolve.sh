#!/bin/bash
# TA-100: Auto-Evolution Engine
# Suggests upgrades or completions based on TA status

REGISTRY="./ta-registry"
STATUS_FILE="$REGISTRY/ta_registry_status.json"
EVOLUTION_LOG="$REGISTRY/proposed_updates.json"

echo "[" > "$EVOLUTION_LOG"
FIRST=true

for dir in $(find "$REGISTRY" -maxdepth 1 -type d -name 'TA-*' | sort); do
  TA_ID=$(basename "$dir")
  CONFIG="$dir/config.json"
  CLI=$(jq -r .CLI_File "$CONFIG")

  if [[ ! -f "$dir/$CLI" ]]; then
    if [ "$FIRST" = false ]; then echo "," >> "$EVOLUTION_LOG"; fi
    FIRST=false
    NAME=$(jq -r .Name "$CONFIG")
    echo "  {"TA_ID": "$TA_ID", "Name": "$NAME", "Status": "needs build"}" >> "$EVOLUTION_LOG"
  fi
done

echo "]" >> "$EVOLUTION_LOG"
echo "🧠 TA-100 Auto-evolution suggestions saved to $EVOLUTION_LOG"
