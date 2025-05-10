
import streamlit as st
import json
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="TA-024v2: Execution Replay + Logger", layout="wide")

st.sidebar.title("⏪ TA Category: Instruction Replay")
assistant = st.sidebar.radio("Choose Assistant", ["TA-024v2: Log + Replay"])

log_path = Path("./ta-registry/TA-024/validation_log.json")
log_path.parent.mkdir(parents=True, exist_ok=True)
if not log_path.exists():
    log_path.write_text("[]")

if assistant == "TA-024v2: Log + Replay":
    st.title("⏪ TA-024 (v2): Replay Last Run + Failure Logger")

    input_prompt = st.text_area("🧠 Input Prompt")
    output_response = st.text_area("📝 Output")

    simulate_fail = st.checkbox("🧪 Flag as Failed Output")

    if st.button("📋 Replay + Log Result"):
        if simulate_fail:
            history = json.load(open(log_path))
            history.append({
                "timestamp": datetime.now().isoformat(),
                "prompt": input_prompt,
                "output": output_response,
                "result": "FAILED"
            })
            json.dump(history, open(log_path, "w"), indent=2)
            st.error("❌ Output flagged + logged to validation_log.json")
        else:
            st.success("✅ Output passed. No error logged.")

    st.markdown("### 📁 Validation Log Preview")
    st.json(json.load(open(log_path)))
