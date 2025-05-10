#!/bin/bash
# Name: Log Execution
# Description: Logs assistant output to ~/ai-assistant-os
# Author: meatheadsmarketing
# Language: bash

PROJECT="project_alpha"
ASSISTANT="summarizer"
DATE=$(date +%Y-%m-%d)
LOGFILE="$HOME/ai-assistant-os/assistant-logs/$PROJECT/$ASSISTANT/input-output-log.md"

mkdir -p "$(dirname "$LOGFILE")"
touch "$LOGFILE"

echo "## Run on ${DATE}" >> "$LOGFILE"
echo "- Instruction Version: v1.1.0" >> "$LOGFILE"
echo "- Prompt: 'Summarize Q2 campaign results'" >> "$LOGFILE"
echo "- Output: 'Impressions +40%, CPL down 12%, Retargeting ROI 5x'" >> "$LOGFILE"
echo "- Memory Used: memory_2025-05-08.json" >> "$LOGFILE"
echo "" >> "$LOGFILE"

open "$LOGFILE"

