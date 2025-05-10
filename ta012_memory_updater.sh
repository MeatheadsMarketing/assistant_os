#!/bin/bash
# @raycast.schemaVersion 1
# @raycast.title TA-012 Memory Updater
# @raycast.mode fullOutput
# @raycast.packageName Assistant OS
# @raycast.description Updates assistant memory.json based on extracted facts
# @raycast.author meatheadsmarketing
# @raycast.language bash

MEMORY_FILE="$HOME/ai-assistant-os/assistant-memory/project_alpha/assistant_001/memory.json"
UPDATE_FACTS="$HOME/ai-assistant-os/assistant-memory/project_alpha/assistant_001/fact_queue.txt"

# Ensure files exist
mkdir -p "$(dirname "$MEMORY_FILE")"
touch "$MEMORY_FILE"
touch "$UPDATE_FACTS"

echo "📥 Reading facts from: $UPDATE_FACTS"
echo ""

# Format and insert facts as new key-value pairs
while IFS= read -r line; do
  KEY=$(echo "$line" | cut -d ':' -f 1 | xargs | tr ' ' '_' | tr '[:upper:]' '[:lower:]')
  VALUE=$(echo "$line" | cut -d ':' -f 2- | xargs)
  echo "  - Adding "$KEY": "$VALUE""
  jq --arg key "$KEY" --arg value "$VALUE" '. + {($key): $value}' "$MEMORY_FILE" > tmp.$$.json && mv tmp.$$.json "$MEMORY_FILE"
done < "$UPDATE_FACTS"

echo ""
echo "✅ Updated memory.json:"
cat "$MEMORY_FILE"
