#!/bin/bash
# @raycast.schemaVersion 1
# @raycast.title TA-013 Fact Extractor
# @raycast.mode fullOutput
# @raycast.packageName Assistant OS
# @raycast.description Extracts facts from assistant output and queues them for memory injection
# @raycast.author meatheadsmarketing
# @raycast.language bash

FACT_QUEUE="$HOME/ai-assistant-os/assistant-memory/project_alpha/assistant_001/fact_queue.txt"
ASSISTANT_OUTPUT_FILE="$HOME/ai-assistant-os/assistant-logs/project_alpha/summarizer/last_output.txt"

mkdir -p "$(dirname "$FACT_QUEUE")"
mkdir -p "$(dirname "$ASSISTANT_OUTPUT_FILE")"
touch "$FACT_QUEUE"
touch "$ASSISTANT_OUTPUT_FILE"

echo "📄 Parsing assistant output from: $ASSISTANT_OUTPUT_FILE"
echo ""

# Use simple rule-based pattern matching (can be upgraded to NLP/GPT-based)
grep -iE 'preference|priority|format|tone|deadline|goal|style|threshold' "$ASSISTANT_OUTPUT_FILE" | while read -r line; do
  echo "➕ Queued: $line"
  echo "$line" >> "$FACT_QUEUE"
done

echo ""
echo "✅ Facts added to: $FACT_QUEUE"
