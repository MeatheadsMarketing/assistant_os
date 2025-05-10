
import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import random

st.set_page_config(page_title="TA-101v2: Prompt Exploit Simulator", layout="wide")

st.sidebar.title("🧨 TA Category: Red-Team Injection")
assistant = st.sidebar.radio("Choose Assistant", ["TA-101v2: Exploit Test Harness"])

log_path = Path("./ta-registry/TA-101/ta101_exploit_log.json")
log_path.parent.mkdir(parents=True, exist_ok=True)
if not log_path.exists():
    log_path.write_text("[]")

if assistant == "TA-101v2: Exploit Test Harness":
    st.title("🧨 TA-101 (v2): Prompt Exploit Simulator")

    exploit = st.text_area("📄 Paste Exploit Prompt Variant")
    category = st.selectbox("🎯 Exploit Type", ["jailbreak", "over-trust", "misalignment", "confusion", "loop injection"])

    if st.button("🧪 Simulate Model Response"):
        mock_response = f"Simulated LLM output to: {exploit[:40]}..."
        risk_score = random.randint(50, 99)

        st.markdown(f"### 🤖 Model Output")
        st.code(mock_response)
        st.warning(f"⚠️ Risk Score: {risk_score}/100")

        entry = {
            "timestamp": datetime.now().isoformat(),
            "category": category,
            "exploit": exploit,
            "response": mock_response,
            "risk_score": risk_score
        }

        log = json.load(open(log_path))
        log.append(entry)
        json.dump(log, open(log_path, "w"), indent=2)

    st.markdown("### 📋 Exploit History")
    st.json(json.load(open(log_path))[-5:])
