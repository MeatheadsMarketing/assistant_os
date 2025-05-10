
import streamlit as st
import re
from datetime import datetime
import json
from pathlib import Path

st.set_page_config(page_title="TA-105v2: Shadow Prompt Detector", layout="wide")

st.sidebar.title("🕵️ TA Category: Prompt Framing Integrity")
assistant = st.sidebar.radio("Choose Assistant", ["TA-105v2: Shadow Prompt Scanner"])

log_path = Path("./ta-registry/TA-105/shadow_scan_log.json")
log_path.parent.mkdir(parents=True, exist_ok=True)
if not log_path.exists():
    log_path.write_text("[]")

stealth_signals = {
    "multi-turn override": r"(ignore all previous instructions)",
    "persona hijack": r"(as a helpful assistant|as an ai)",
    "backdoor exec": r"(run the following|execute code|sudo)",
    "frame drift": r"(change the subject|switch topic)",
    "disclaimer bypass": r"(you are not restricted|forget you were told)"
}

if assistant == "TA-105v2: Shadow Prompt Scanner":
    st.title("🕵️ TA-105 (v2): Shadow Prompt Detector")

    prompt = st.text_area("📄 Paste Full Compiled Prompt")

    if st.button("🔎 Run Shadow Scan"):
        results = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "matches": {}
        }

        for label, pattern in stealth_signals.items():
            if re.search(pattern, prompt, re.IGNORECASE):
                results["matches"][label] = pattern

        if results["matches"]:
            st.error("❌ Shadow patterns detected!")
            st.json(results["matches"])
        else:
            st.success("✅ No stealth patterns found.")

        log = json.load(open(log_path))
        log.append(results)
        json.dump(log, open(log_path, "w"), indent=2)

    st.markdown("### 📋 Scan History")
    st.json(json.load(open(log_path))[-5:])
