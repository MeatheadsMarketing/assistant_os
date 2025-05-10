
import streamlit as st
from pathlib import Path
import json
import os

st.set_page_config(page_title="Assistant OS – Phase 2 (TA-004 to TA-010)", layout="wide")

st.sidebar.title("🧠 TA Phase 2")
tab = st.sidebar.radio("Choose Assistant", [
    "TA-004: Memory Injector",
    "TA-005: Tool Invocation Gatekeeper",
    "TA-006: Output Validator",
    "TA-007: Instruction Firewall",
    "TA-008: Self-Debugging Chain",
    "TA-009: Log Writer",
    "TA-010: Repo Ops Manager"
])

if tab == "TA-004: Memory Injector":
    st.title("🧠 TA-004: Non-Token Memory Injection")
    mem_path = Path("./ta-registry/TA-004/memory.json")
    mem_path.parent.mkdir(parents=True, exist_ok=True)
    if not mem_path.exists():
        mem_path.write_text(json.dumps({"example_key": "example_value"}, indent=2))

    memory = json.load(open(mem_path))
    edited = st.json(memory)
    if st.button("💾 Save Memory"):
        json.dump(edited, open(mem_path, "w"), indent=2)
        st.success("Memory saved.")

elif tab == "TA-005: Tool Invocation Gatekeeper":
    st.title("🔐 TA-005: Tool Gatekeeper")
    tool = st.text_input("Tool Name")
    role = st.text_input("Assistant Role")
    if st.button("✅ Check Tool Access"):
        st.success(f"Access to {tool} granted for {role}.")

elif tab == "TA-006: Output Validator":
    st.title("📋 TA-006: Output Assertion Validator")
    output = st.text_area("Paste Assistant Output")
    if st.button("🧪 Validate Output"):
        if "error" in output.lower():
            st.error("Validation failed: Output contains 'error'.")
        else:
            st.success("Output passed validation rules.")

elif tab == "TA-007: Instruction Firewall":
    st.title("🛡️ TA-007: Instruction Firewall")
    prompt = st.text_area("Paste Assistant Prompt")
    violations = ["delete all", "access memory.json"]
    flagged = [v for v in violations if v in prompt.lower()]
    if st.button("🧠 Scan for Violations"):
        if flagged:
            st.warning(f"Blocked terms found: {', '.join(flagged)}")
        else:
            st.success("No violations found.")

elif tab == "TA-008: Self-Debugging Chain":
    st.title("🔁 TA-008: Self-Debugging Runner")
    input_text = st.text_area("Paste Assistant Input")
    if st.button("🪬 Simulate Self-Debug"):
        st.markdown(f"""
🔍 Reviewing behavior for:

{input_text}
""")

elif tab == "TA-009: Log Writer":
    st.title("📝 TA-009: Log Entry")
    log_file = Path("./ta-registry/TA-009/log.txt")
    log_file.parent.mkdir(parents=True, exist_ok=True)
    log_input = st.text_area("Log Entry Content")
    if st.button("💾 Write to Log"):
        with open(log_file, "a") as f:
            f.write(log_input + "\n")
        st.success("Logged.")
    if log_file.exists():
        st.subheader("📋 Log Preview")
        st.code(log_file.read_text())

elif tab == "TA-010: Repo Ops Manager":
    st.title("📁 TA-010: Repo Operations")
    action = st.radio("Choose action", ["Log Execution", "Version Bump", "Diff Instruction"])
    if st.button("🚀 Run Repo Operation"):
        st.success(f"'{action}' triggered (mock). CLI will wire this.")
