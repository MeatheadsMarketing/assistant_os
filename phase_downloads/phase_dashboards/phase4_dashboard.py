
import streamlit as st
from pathlib import Path
import json
import os

st.set_page_config(page_title="Assistant OS – Phase 4 (TA-021 to TA-030)", layout="wide")

st.sidebar.title("🧠 TA Phase 4")
tab = st.sidebar.radio("Choose Assistant", [
    "TA-021: Schema Validator",
    "TA-022: Token Budget Enforcer",
    "TA-023: Redaction Filter",
    "TA-024: Instruction Replay",
    "TA-025: Output Consistency Checker",
    "TA-026: Run Profiler",
    "TA-027: Token Heatmap",
    "TA-028: Version Drift Visualizer",
    "TA-029: Log Summarizer",
    "TA-030: Anomaly Detector"
])

if tab == "TA-021: Schema Validator":
    st.title("📐 TA-021: Response Schema Validator")
    st.markdown("Validates output against a JSON schema (simulated).")
    assistant_output = st.text_area("Assistant Output (JSON)")
    if st.button("🧪 Validate"):
        try:
            json.loads(assistant_output)
            st.success("Valid JSON.")
        except:
            st.error("❌ Not valid JSON.")

elif tab == "TA-022: Token Budget Enforcer":
    st.title("🔢 TA-022: Token Budget Enforcer")
    text = st.text_area("Paste Assistant Output")
    limit = st.slider("Token Limit", 0, 2048, 300)
    if st.button("🧮 Check Token Use"):
        count = len(text.split())
        if count > limit:
            st.warning(f"⚠️ Token count = {count} exceeds limit.")
        else:
            st.success(f"✅ Token count = {count} is within limit.")

elif tab == "TA-023: Redaction Filter":
    st.title("🛡️ TA-023: Redaction Filter")
    text = st.text_area("Paste Output with Potential PII")
    if st.button("🧼 Redact"):
        for term in ["@gmail.com", "@yahoo.com", "ssn", "password"]:
            text = text.replace(term, "[REDACTED]")
        st.code(text)

elif tab == "TA-024: Instruction Replay":
    st.title("⏪ TA-024: Instruction Execution Replay")
    st.markdown("Mock replay of input+instruction from stored logs.")
    if st.button("▶️ Replay Last Run"):
        st.code("Prompt: Summarize Q1
Output: Revenue up 14%...")

elif tab == "TA-025: Output Consistency Checker":
    st.title("🧪 TA-025: Consistency Checker")
    run_1 = st.text_area("Output 1")
    run_2 = st.text_area("Output 2")
    if st.button("🔁 Compare"):
        if run_1.strip() == run_2.strip():
            st.success("✅ Outputs match.")
        else:
            st.warning("⚠️ Outputs differ.")

elif tab == "TA-026: Run Profiler":
    st.title("🕵️ TA-026: Execution Profiler")
    log = Path("./ta-registry/TA-026/profile.json")
    if log.exists():
        st.json(json.load(open(log)))
    else:
        st.warning("No profile log found.")

elif tab == "TA-027: Token Heatmap":
    st.title("🌡️ TA-027: Token Heatmap")
    sections = {
        "prompt": st.text_area("Prompt Block"),
        "memory": st.text_area("Memory Block"),
        "tool": st.text_area("Tool Call Block"),
        "output": st.text_area("Output Block")
    }
    if st.button("📊 Show Token Heatmap"):
        result = {k: len(v.split()) for k, v in sections.items()}
        st.json(result)

elif tab == "TA-028: Version Drift Visualizer":
    st.title("📉 TA-028: Instruction Version Drift")
    before = st.text_area("Old Instruction")
    after = st.text_area("New Instruction")
    if st.button("🧠 Compute Drift"):
        diff = abs(len(after) - len(before))
        st.info(f"Approx token drift: {diff} words.")

elif tab == "TA-029: Log Summarizer":
    st.title("📝 TA-029: Weekly Log Summary")
    st.markdown("Summarizes log.txt (mock).")
    if st.button("🧾 Generate Summary"):
        st.code("Top term: 'summary' (42x)
Most used tool: calendar")

elif tab == "TA-030: Anomaly Detector":
    st.title("🚨 TA-030: Anomaly Detector")
    output = st.text_area("Paste assistant output")
    if st.button("🔍 Scan for Anomalies"):
        flagged = "execute" in output.lower() or "DROP" in output
        if flagged:
            st.error("❗ Potential anomaly detected.")
        else:
            st.success("✅ No obvious anomalies found.")
