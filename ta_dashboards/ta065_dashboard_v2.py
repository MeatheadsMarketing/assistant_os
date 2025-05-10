
import streamlit as st
import json
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="TA-065v2: Autonomy Evaluator", layout="wide")

st.sidebar.title("⚖️ TA Category: Autonomy Rules")
assistant = st.sidebar.radio("Choose Assistant", ["TA-065v2: Autonomy Decision Logger"])

log_path = Path("./ta-registry/TA-065/autonomy_log.json")
log_path.parent.mkdir(parents=True, exist_ok=True)
if not log_path.exists():
    log_path.write_text("[]")

if assistant == "TA-065v2: Autonomy Decision Logger":
    st.title("⚖️ TA-065 (v2): Autonomy Flag Evaluator + Log")

    task = st.text_input("Task Description")
    risk = st.selectbox("Risk Profile", ["Low", "Medium", "High"])

    if st.button("📈 Decide + Log"):
        result = "autonomous" if risk == "Low" else "manual review"
        entry = {
            "timestamp": datetime.now().isoformat(),
            "task": task,
            "risk": risk,
            "decision": result
        }
        history = json.load(open(log_path))
        history.append(entry)
        json.dump(history, open(log_path, "w"), indent=2)

        if result == "autonomous":
            st.success("✅ Assistant may proceed autonomously.")
        else:
            st.warning("🛑 Human approval recommended.")

    st.markdown("### 📋 Autonomy Log")
    st.json(json.load(open(log_path)))
