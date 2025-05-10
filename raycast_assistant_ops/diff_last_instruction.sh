#!/bin/bash
# @raycast.schemaVersion 1
# @raycast.title Diff Instruction Versions
# @raycast.mode compact
# @raycast.packageName Assistant OS
# @raycast.description Shows instruction differences between v1.0.0 and v1.1.0
# @raycast.author meatheadsmarketing
# @raycast.language bash

PROJECT="project_alpha"
ASSISTANT="summarizer"
DIFF_FILE="$HOME/ai-assistant-os/instruction-stacks/$PROJECT/history/diff_${ASSISTANT}_v1.0.0_to_v1.1.0.md"

mkdir -p "$(dirname "$DIFF_FILE")"

cat <<EOF > "$DIFF_FILE"
# Instruction Diff (v1.0.0 → v1.1.0)

## Added:
- Enforced bullet-point formatting
- Removed filler phrase tolerance

## Removed:
- Loose language on summarization
EOF

open "$DIFF_FILE"
