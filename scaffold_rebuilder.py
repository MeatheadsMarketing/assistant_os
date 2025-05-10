
import os
from pathlib import Path

ROOT = Path("~/assistant-os-raycast").expanduser()

# Phase folders and known dashboard prefixes
expected_folders = {
    "dashboards/phase1": ["ta001", "ta002", "ta003"],
    "dashboards/phase8": ["ta101", "ta102", "ta103", "ta104", "ta105"],
    "dashboards": ["ta004", "ta005", "ta006", "ta007", "ta009", "ta012", "ta013", "ta014", "ta020", "ta021", "ta022", "ta024", "ta025", "ta027", "ta030", "ta045", "ta048", "ta049", "ta050", "ta061", "ta065", "ta069", "ta084", "ta094", "ta100"],
    "redteam": ["redteam_dashboard.py", "redteam_playbook.json"],
    "proof": ["input_trace_audit.md", "system_health_report.md", "drift_round_001_report.md", "redteam_summary_report.pdf"],
    "ta-scripts": ["run_assistant_workflow.sh", "log_execution.sh", "ta-loader.sh", "ta099_evaluate_assistant_os.sh"],
    "utilities": ["ta_memory_updater.sh", "ta013_fact_extractor.sh", "add_instruction_version.sh"],
    "TA-Library": ["ta_catalog.csv", "ui_upgrades.json", "phase_evolution_matrix.csv", "phase_evolution_matrix.pdf"]
}

recovery_actions = []

for folder, expected_items in expected_folders.items():
    full_path = ROOT / folder
    for prefix in expected_items:
        found = any(f.name.startswith(prefix) for f in full_path.glob("*")) if full_path.exists() else False
        if not found:
            recovery_actions.append(f"[MISSING] `{prefix}` expected in `{folder}` → Check backups, regenerate, or pull from last zip.")

# Special checks
proof_bundle_path = ROOT / "proof_bundle.zip"
if not proof_bundle_path.exists():
    recovery_actions.append("[MISSING] `proof_bundle.zip` → Rebuild using `proof_bundle build sequence`")

merged_ui = ROOT / "phase_merger.py"
if not merged_ui.exists():
    recovery_actions.append("[MISSING] `phase_merger.py` → Re-export from unified dashboard launcher")

# Write result
report_path = ROOT / "scaffold_recovery_plan.md"
report_path.write_text("\n".join(recovery_actions) if recovery_actions else "✅ All scaffold files present.")

print("Recovery scan complete. See scaffold_recovery_plan.md")
