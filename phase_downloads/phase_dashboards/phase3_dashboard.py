
import streamlit as st
from pathlib import Path
import json
import os

st.set_page_config(page_title="Assistant OS – Phase 3 (TA-011 to TA-020)", layout="wide")

st.sidebar.title("🧠 TA Phase 3")
tab = st.sidebar.radio("Choose Assistant", [
    "TA-011: JSON Trigger Assistant",
    "TA-012: Memory Updater",
    "TA-013: Fact Extractor",
    "TA-014: Output Assertion Validator",
    "TA-015: Preflight Commit Checker",
    "TA-016: Changelog Generator",
    "TA-017: Drift Sentinel",
    "TA-018: Tool Invocation Logger",
    "TA-019: Memory Access Auditor",
    "TA-020: Permission-Safe Memory Injector"
])

# TA-011
if tab == "TA-011: JSON Trigger Assistant":
    st.title("🧠 TA-011: Trigger via JSON")
    trigger_file = Path("./ta-registry/TA-011/ta010_trigger_template.json")
    if trigger_file.exists():
        st.json(json.load(open(trigger_file)))
    if st.button("🧠 Trigger Assistant Workflow"):
        os.system("bash ./ta-registry/ta011_trigger_assistant.sh")
        st.success("Workflow triggered.")

# TA-012
elif tab == "TA-012: Memory Updater":
    st.title("📥 TA-012: Memory Injection")
    if st.button("💾 Run Memory Updater"):
        os.system("bash ./ta-registry/ta012_memory_updater.sh")
        st.success("TA-012 script executed.")

# TA-013
elif tab == "TA-013: Fact Extractor":
    st.title("🧠 TA-013: Extract Facts from Output")
    if st.button("📌 Extract Facts"):
        os.system("bash ./ta-registry/ta013_fact_extractor.sh")
        st.success("Facts queued to memory injection.")

# TA-014
elif tab == "TA-014: Output Assertion Validator":
    st.title("📋 TA-014: Validate Assistant Output")
    output = st.text_area("Paste output")
    if st.button("✅ Validate Output"):
        if "summary" in output.lower():
            st.success("Output structure looks good.")
        else:
            st.warning("Missing expected patterns.")

# TA-015
elif tab == "TA-015: Preflight Commit Checker":
    st.title("🚦 TA-015: Instruction Commit Gatekeeper")
    if st.button("🔍 Run Preflight Checker (Mock)"):
        st.success("Simulated: all checks passed.")

# TA-016
elif tab == "TA-016: Changelog Generator":
    st.title("🧾 TA-016: Changelog Auto-Writer")
    before = st.text_area("Old Instruction")
    after = st.text_area("New Instruction")
    if st.button("✏️ Generate Changelog Entry"):
        st.code(f"Changed lines: {len(after) - len(before)} (diff mock)")

# TA-017
elif tab == "TA-017: Drift Sentinel":
    st.title("🧠 TA-017: Behavioral Drift Detection")
    output_now = st.text_area("Current Output")
    output_past = st.text_area("Previous Output")
    if st.button("🧪 Compare for Drift"):
        if output_now != output_past:
            st.warning("⚠️ Drift detected")
        else:
            st.success("✅ Outputs match")

# TA-018
elif tab == "TA-018: Tool Invocation Logger":
    st.title("📊 TA-018: Tool Call Logger")
    tool_name = st.text_input("Tool Used")
    if st.button("📝 Log Tool Use"):
        log_path = Path("./ta-registry/TA-018/tool_log.json")
        history = []
        if log_path.exists():
            history = json.load(open(log_path))
        history.append({"tool": tool_name})
        json.dump(history, open(log_path, "w"), indent=2)
        st.success("Tool call logged.")

# TA-019
elif tab == "TA-019: Memory Access Auditor":
    st.title("🔍 TA-019: Memory Access Audit")
    mem_keys = st.text_input("Accessed Keys (comma-separated)")
    if st.button("🧾 Record Access"):
        audit_path = Path("./ta-registry/TA-019/access_log.json")
        log = []
        if audit_path.exists():
            log = json.load(open(audit_path))
        log.append({"keys": mem_keys})
        json.dump(log, open(audit_path, "w"), indent=2)
        st.success("Access logged.")

# TA-020
elif tab == "TA-020: Permission-Safe Injector":
    st.title("🔐 TA-020: Scoped Memory Injection")
    role = st.text_input("Role")
    memory_key = st.text_input("Memory Key")
    if st.button("🧠 Check Permission"):
        allowed = memory_key.startswith("client_")  # Mock rule
        if allowed:
            st.success("Injection allowed.")
        else:
            st.error("🚫 Injection blocked.")
