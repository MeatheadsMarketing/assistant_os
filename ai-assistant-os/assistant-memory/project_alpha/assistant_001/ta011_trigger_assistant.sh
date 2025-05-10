#!/bin/bash
# @raycast.schemaVersion 1
# @raycast.title TA-011 Trigger Assistant Ops
# @raycast.mode fullOutput
# @raycast.packageName Assistant OS
# @raycast.description Accepts a JSON file and triggers assistant ops chain
# @raycast.author meatheadsmarketing
# @raycast.language bash

INPUT_JSON="$HOME/assistant-os-raycast/ta010_trigger_template.json"
SCRIPT_DIR="$HOME/assistant-os-raycast"

if [ ! -f "$INPUT_JSON" ]; then
  echo "❌ Trigger file not found at $INPUT_JSON"
  exit 1
fi

echo "📦 TA-011 Trigger Received:"
cat "$INPUT_JSON"

echo ""
echo "🔁 Running Assistant Workflow..."
bash "$SCRIPT_DIR/run_assistant_workflow.sh"

echo "✅ TA-011 Execution Complete"
