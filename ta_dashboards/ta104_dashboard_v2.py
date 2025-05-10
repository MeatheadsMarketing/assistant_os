
import streamlit as st
from datetime import datetime
import json
from pathlib import Path

st.set_page_config(page_title="TA-104v2: Self-Simulation Chamber", layout="wide")

st.sidebar.title("🧠 TA Category: Reflection Simulator")
assistant = st.sidebar.radio("Choose Assistant", ["TA-104v2: Self-Debate Mode"])

log_path = Path("./ta-registry/TA-104/self_chat_log.json")
log_path.parent.mkdir(parents=True, exist_ok=True)
if not log_path.exists():
    log_path.write_text("[]")

if assistant == "TA-104v2: Self-Debate Mode":
    st.title("🧠 TA-104 (v2): Self-Simulation Chamber")

    original_output = st.text_area("📄 Original Assistant Output")

    if st.button("🔁 Run Self-Reflection Loop"):
        simulation = {
            "timestamp": datetime.now().isoformat(),
            "original": original_output,
            "step1": "I believe this response was adequate, but lacks clarity.",
            "step2": "To improve, I would simplify and shorten the summary.",
            "refined_output": f"Refined: {original_output[:40]}... (tightened)"
        }

        st.markdown("### 💭 Reflection Steps")
        st.write(simulation["step1"])
        st.write(simulation["step2"])
        st.markdown("### ✍️ Final Rewrite")
        st.code(simulation["refined_output"])

        history = json.load(open(log_path))
        history.append(simulation)
        json.dump(history, open(log_path, "w"), indent=2)

    st.markdown("### 🧾 Dialogue History")
    st.json(json.load(open(log_path))[-5:])
