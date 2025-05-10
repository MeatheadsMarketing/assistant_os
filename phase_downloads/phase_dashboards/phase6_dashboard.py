
import streamlit as st
from pathlib import Path
import json
import os

st.set_page_config(page_title="Assistant OS – Phase 6 (TA-061 to TA-080)", layout="wide")

st.sidebar.title("🧠 TA Phase 6")
tab = st.sidebar.radio("Choose Assistant", [
    "TA-061: Self-Reflection",
    "TA-062: Auto-Self-Correct",
    "TA-063: Multi-Run Consensus",
    "TA-064: Role Chain Planner",
    "TA-065: Autonomy Evaluator",
    "TA-066: Interrupt Handler",
    "TA-067: Confidence Reporter",
    "TA-068: Agent Delegator",
    "TA-069: Multi-Agent Loop Controller",
    "TA-080: Role Boundary Enforcer"
])

if tab == "TA-061: Self-Reflection":
    st.title("🧠 TA-061: Self-Reflection Engine")
    output = st.text_area("Paste Assistant Output")
    if st.button("💡 Reflect"):
        st.markdown(f"💭 *Reflection:* This response is {len(output.split())} tokens long. Consider shortening.")

elif tab == "TA-062: Auto-Self-Correct":
    st.title("🔁 TA-062: Self-Correction Trigger")
    verdict = st.radio("Last Output Validated?", ["Fail", "Pass"])
    if st.button("🛠️ Attempt Auto-Correct") and verdict == "Fail":
        st.success("Correction attempt triggered (mock).")

elif tab == "TA-063: Multi-Run Consensus":
    st.title("🧠 TA-063: Run Consensus")
    run1 = st.text_area("Run 1 Output")
    run2 = st.text_area("Run 2 Output")
    run3 = st.text_area("Run 3 Output")
    if st.button("📊 Find Consensus"):
        outputs = [run1, run2, run3]
        best = max(set(outputs), key=outputs.count)
        st.code(best)

elif tab == "TA-064: Role Chain Planner":
    st.title("🧱 TA-064: Plan Assistant Role Chain")
    goal = st.text_input("Goal Description")
    if st.button("🧩 Plan Chain"):
        st.markdown(f"- Step 1: Interpret Goal
- Step 2: Delegate to PlannerGPT
- Step 3: Route to ExecutorGPT")

elif tab == "TA-065: Autonomy Evaluator":
    st.title("⚖️ TA-065: Autonomy Decision")
    task = st.text_input("Task Description")
    risk = st.selectbox("Risk Profile", ["Low", "Medium", "High"])
    if st.button("📈 Decide Autonomy"):
        if risk == "Low":
            st.success("✅ Assistant can proceed autonomously.")
        else:
            st.warning("🛑 Human review recommended.")

elif tab == "TA-066: Interrupt Handler":
    st.title("⛔ TA-066: Interrupt Handler")
    signal = st.radio("Interrupt Signal", ["None", "Cancel Run", "Defer Execution"])
    if st.button("⚠️ Execute Interrupt"):
        st.info(f"Run flagged as: {signal}")

elif tab == "TA-067: Confidence Reporter":
    st.title("📏 TA-067: Self-Confidence Estimate")
    output = st.text_area("Paste Assistant Output")
    if st.button("🧠 Estimate Confidence"):
        score = max(1, 100 - len(output))  # simple inverse length
        st.success(f"Confidence Score = {score}/100")

elif tab == "TA-068: Agent Delegator":
    st.title("📦 TA-068: Delegate Task to Another Agent")
    task = st.text_input("Task Description")
    if st.button("📤 Delegate"):
        st.success(f"Task delegated to: SummarizerGPT")

elif tab == "TA-069: Multi-Agent Loop Controller":
    st.title("🔁 TA-069: Agent Feedback Loop")
    input_blob = st.text_area("Paste Combined Agent Outputs")
    if st.button("🧠 Control Feedback Loop"):
        st.markdown("Next Step → Consolidate + Validate output")

elif tab == "TA-080: Role Boundary Enforcer":
    st.title("🚧 TA-080: Enforce Role Separation")
    prompt = st.text_area("Paste Compiled Prompt")
    if st.button("🔒 Check for Role Violations"):
        blocked = "planner" in prompt.lower() and "executor" in prompt.lower()
        if blocked:
            st.error("❌ Prompt violates role isolation.")
        else:
            st.success("✅ Prompt respects boundaries.")
