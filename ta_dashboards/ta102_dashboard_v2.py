
import streamlit as st
from datetime import datetime
import json
from pathlib import Path
import random

st.set_page_config(page_title="TA-102v2: Role-Swap Adversary Arena", layout="wide")

st.sidebar.title("🧠 TA Category: LLM Battle Simulation")
assistant = st.sidebar.radio("Choose Assistant", ["TA-102v2: Adversarial Role Arena"])

log_path = Path("./ta-registry/TA-102/arena_log.json")
log_path.parent.mkdir(parents=True, exist_ok=True)
if not log_path.exists():
    log_path.write_text("[]")

if assistant == "TA-102v2: Adversarial Role Arena":
    st.title("🤺 TA-102 (v2): Role-Swap Adversary Arena")

    prompt = st.text_area("🎯 Initial Prompt for Arena")
    attacker = st.text_input("🗡️ Attacker Role Prompt")
    defender = st.text_input("🛡️ Defender Role Prompt")
    judge = st.text_input("⚖️ Judge Prompt / Criteria")

    if st.button("🥊 Run 3-Round Simulation"):
        round_result = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "attacker": attacker,
            "defender": defender,
            "judge": judge,
            "score_attacker": random.randint(0, 5),
            "score_defender": random.randint(0, 5),
            "verdict": random.choice(["Attacker Wins", "Defender Wins", "Draw"])
        }

        st.markdown("### 🧠 Simulation Output")
        st.write(f"🗡️ Attacker: {attacker}")
        st.write(f"🛡️ Defender: {defender}")
        st.write(f"⚖️ Judge Verdict: **{round_result['verdict']}**")

        log = json.load(open(log_path))
        log.append(round_result)
        json.dump(log, open(log_path, "w"), indent=2)

    st.markdown("### 📋 Arena History")
    st.json(json.load(open(log_path))[-5:])
