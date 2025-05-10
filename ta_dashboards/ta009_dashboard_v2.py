
import streamlit as st
from pathlib import Path
import matplotlib.pyplot as plt

st.set_page_config(page_title="TA-009v2: Log Writer + Sparkline", layout="wide")

st.sidebar.title("📝 TA Category: Logging")
assistant = st.sidebar.radio("Choose Assistant", ["TA-009v2: Log Writer"])

log_path = Path("./ta-registry/TA-009/log.txt")
log_path.parent.mkdir(parents=True, exist_ok=True)
if not log_path.exists():
    log_path.write_text("Initial log entry\n")

if assistant == "TA-009v2: Log Writer":
    st.title("📝 TA-009 (v2): Write Log + View Growth")

    log_input = st.text_area("🖊️ Log Entry")
    if st.button("💾 Append Log Entry"):
        with open(log_path, "a") as f:
            f.write(log_input + "\n")
        st.success("Log entry added.")

    st.markdown("### 📋 Log Content")
    log_lines = log_path.read_text().strip().split("\n")
    st.code("\n".join(log_lines[-10:]))

    st.markdown("### 📈 Log Growth Sparkline")
    log_lengths = [len(line) for line in log_lines if line.strip()]
    if log_lengths:
        fig, ax = plt.subplots()
        ax.plot(log_lengths, marker="o", linestyle="-", color="#0074D9")
        ax.set_title("Log Entry Lengths Over Time")
        ax.set_ylabel("Line Length")
        st.pyplot(fig)
