#!/bin/bash

# ta-loader.sh: CLI utility to view, run, or initialize Tiny Assistants from the TA Registry
# Usage:
#   ./ta-loader.sh list
#   ./ta-loader.sh show TA-042
#   ./ta-loader.sh init TA-042
#   ./ta-loader.sh run TA-042

REGISTRY="./ta-registry"
CMD=$1
TA_ID=$2

if [[ "$CMD" == "list" ]]; then
  echo "Available Assistants:"
  find "$REGISTRY" -type d -name 'TA-*' | sort
elif [[ "$CMD" == "show" ]]; then
  cat "$REGISTRY/$TA_ID/config.json"
elif [[ "$CMD" == "init" ]]; then
  TA_PATH="$REGISTRY/$TA_ID"
  if [[ -f "$TA_PATH/config.json" ]]; then
    NAME=$(jq -r .Name "$TA_PATH/config.json")
    PURPOSE=$(jq -r .Purpose "$TA_PATH/config.json")
    CLI_FILE=$(jq -r .CLI_File "$TA_PATH/config.json")

    echo "# $NAME" > "$TA_PATH/README.md"
    echo "" >> "$TA_PATH/README.md"
    echo "## Purpose" >> "$TA_PATH/README.md"
    echo "$PURPOSE" >> "$TA_PATH/README.md"
    echo "" >> "$TA_PATH/README.md"
    echo "## Usage" >> "$TA_PATH/README.md"
    echo "\\`./$CLI_FILE\\`" >> "$TA_PATH/README.md"

    touch "$TA_PATH/$CLI_FILE"
    chmod +x "$TA_PATH/$CLI_FILE"
    echo "#!/bin/bash" > "$TA_PATH/$CLI_FILE"
    echo "# Stub for $TA_ID: $NAME" >> "$TA_PATH/$CLI_FILE"
    echo "echo Running $TA_ID..." >> "$TA_PATH/$CLI_FILE"
    echo "echo (Placeholder script)" >> "$TA_PATH/$CLI_FILE"

    echo "✅ Initialized $TA_ID in $TA_PATH"
  else
    echo "❌ $TA_ID not found in registry."
  fi
elif [[ "$CMD" == "run" ]]; then
  TA_PATH="$REGISTRY/$TA_ID"
  CLI_FILE=$(jq -r .CLI_File "$TA_PATH/config.json")
  bash "$TA_PATH/$CLI_FILE"
else
  echo "Unknown command: $CMD"
fi
