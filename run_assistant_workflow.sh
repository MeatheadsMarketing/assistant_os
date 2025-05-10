#!/bin/bash
# @raycast.schemaVersion 1
# @raycast.title Run Full Assistant Ops
# @raycast.mode compact
# @raycast.packageName Assistant OS
# @raycast.description Executes versioning, logging, and diffing as a chain
# @raycast.author meatheadsmarketing
# @raycast.language bash

SCRIPT_DIR="$HOME/assistant-os-raycast"

echo "Running: Add Instruction Version"
bash "$SCRIPT_DIR/add_instruction_version.sh"

echo "Running: Log Execution"
bash "$SCRIPT_DIR/log_execution.sh"

echo "Running: Diff Instruction Versions"
bash "$SCRIPT_DIR/diff_last_instruction.sh"

echo "✅ Assistant Ops Completed"
