#!/bin/bash
# @raycast.schemaVersion 1
# @raycast.title Add Instruction Version
# @raycast.mode compact
# @raycast.packageName Assistant OS
# @raycast.description Adds a new instruction version and logs it
# @raycast.author meatheadsmarketing
# @raycast.language bash

PROJECT="project_alpha"
ASSISTANT="summarizer"
VERSION="v1.1.0"
DATE=$(date +%Y-%m-%d)

INSTRUCTION_FILE="$HOME/ai-assistant-os/instruction-stacks/$PROJECT/sub_roles/${ASSISTANT}_${VERSION}.md"
CHANGELOG_FILE="$HOME/ai-assistant-os/instruction-stacks/$PROJECT/history/changelog.md"

mkdir -p "$(dirname "$INSTRUCTION_FILE")"
mkdir -p "$(dirname "$CHANGELOG_FILE")"

echo "- Reduce verbosity aggressively." > "$INSTRUCTION_FILE"
echo "- Output exactly 3 bullet points." >> "$INSTRUCTION_FILE"
echo "[${VERSION}] - ${DATE} - architect: Added version via Raycast" >> "$CHANGELOG_FILE"

open "$INSTRUCTION_FILE"
