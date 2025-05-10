# 🧠 Assistant OS: TA Registry Index

This is the full index of all Tiny Assistants (TAs) in your modular AI operating system.

Each TA follows a microservice-like pattern:
- 🔧 Shell-executable from CLI
- ⚡ Raycast-triggerable
- 📁 Modular per-directory deployment
- 🧩 Config-driven with `config.json`
- 🧠 Traceable via `ta_registry_status.json` or `ta099_evaluate_assistant_os.sh`

---
## 📂 Assistant Index
| TA ID | Name | Domain | CLI File | Config Path |
|-------|------|--------|----------|-------------|
| TA-014 | Output Assertion Validator | VAL | `ta014_output_assertion.sh` | `./ta-registry/TA-014/config.json` |
| TA-015 | Preflight Commit Checker | OPS | `ta015_preflight_checker.sh` | `./ta-registry/TA-015/config.json` |
| TA-016 | Auto-Changelog Generator | OPS | `ta016_changelog_generator.sh` | `./ta-registry/TA-016/config.json` |
| TA-017 | Instruction Drift Sentinel | VAL | `ta017_drift_sentinel.sh` | `./ta-registry/TA-017/config.json` |
| TA-018 | Tool Invocation Logger | LOG | `ta018_tool_logger.sh` | `./ta-registry/TA-018/config.json` |
| TA-019 | Memory Access Auditor | LOG | `ta019_memory_auditor.sh` | `./ta-registry/TA-019/config.json` |
| TA-020 | Permission-Safe Memory Injector | SEC | `ta020_memory_permission_checker.sh` | `./ta-registry/TA-020/config.json` |
| TA-021 | Response Schema Validator | VAL | `ta021_schema_validator.sh` | `./ta-registry/TA-021/config.json` |
| TA-022 | Token Budget Enforcer | VAL | `ta022_token_enforcer.sh` | `./ta-registry/TA-022/config.json` |
| TA-023 | Redaction Filter | VAL | `ta023_redactor.sh` | `./ta-registry/TA-023/config.json` |
| TA-024 | Instruction Execution Replay | LOG | `ta024_replay_runner.sh` | `./ta-registry/TA-024/config.json` |
| TA-025 | Run Consistency Comparator | VAL | `ta025_output_consistency.sh` | `./ta-registry/TA-025/config.json` |
| TA-026 | Assistant Run Profiler | LOG | `ta026_run_profiler.sh` | `./ta-registry/TA-026/config.json` |
| TA-027 | Token Heatmap Generator | LOG | `ta027_token_heatmap.sh` | `./ta-registry/TA-027/config.json` |
| TA-028 | Version Drift Visualizer | LOG | `ta028_version_diff_viz.sh` | `./ta-registry/TA-028/config.json` |
| TA-029 | Log Summarizer | LOG | `ta029_log_summarizer.sh` | `./ta-registry/TA-029/config.json` |
| TA-030 | Anomaly Detector | VAL | `ta030_anomaly_detector.sh` | `./ta-registry/TA-030/config.json` |
| TA-031 | Instruction Usage Tracker | LOG | `ta031_usage_tracker.sh` | `./ta-registry/TA-031/config.json` |
| TA-032 | Prompt Diff Tracker | LOG | `ta032_prompt_diff_tracker.sh` | `./ta-registry/TA-032/config.json` |
| TA-033 | Assistant Failure Log | LOG | `ta033_failure_logger.sh` | `./ta-registry/TA-033/config.json` |
| TA-034 | Memory Key Frequency Analyzer | LOG | `ta034_memory_key_frequency.sh` | `./ta-registry/TA-034/config.json` |
| TA-035 | Instruction Usage Heatmap | LOG | `ta035_instruction_heatmap.sh` | `./ta-registry/TA-035/config.json` |
| TA-036 | Output Tone Profiler | LOG | `ta036_tone_profiler.sh` | `./ta-registry/TA-036/config.json` |
| TA-037 | Top Prompt Tracker | LOG | `ta037_prompt_tracker.sh` | `./ta-registry/TA-037/config.json` |
| TA-038 | Response Length Monitor | LOG | `ta038_length_monitor.sh` | `./ta-registry/TA-038/config.json` |
| TA-039 | Instruction Reference Mapper | LOG | `ta039_reference_mapper.sh` | `./ta-registry/TA-039/config.json` |
| TA-040 | Log Data Compressor | LOG | `ta040_log_compressor.sh` | `./ta-registry/TA-040/config.json` |