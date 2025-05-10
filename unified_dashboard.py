
import streamlit as st
import subprocess

st.set_page_config(page_title="Assistant OS Launcher", layout="centered")

st.title("🧠 Assistant OS: Unified Dashboard")

st.markdown("""
Welcome to the control center. Use this launcher to access any phase-based TA dashboard.

## 📂 Dashboards Available
- Phase 1: TA-001 to TA-003
- Phase 2: TA-004 to TA-010
- Phase 3: TA-011 to TA-020
- Phase 4: TA-021 to TA-030
- Phase 5: TA-041 to TA-050
- Phase 6: TA-061 to TA-080
- Phase 7: TA-081 to TA-100
""")

phase = st.selectbox("Choose a TA Phase to Launch", [
    "starter_suite_dashboard.py",
    "phase2_dashboard.py",
    "phase3_dashboard.py",
    "phase4_dashboard.py",
    "phase5_dashboard.py",
    "phase6_dashboard.py",
    "phase7_dashboard.py"
])

st.markdown("📁 Make sure the selected file is in your project root.")

if st.button("🚀 Launch Selected Dashboard"):
    st.markdown(f"Launching: `{phase}` — open this in your terminal:")
    st.code(f"streamlit run {phase}")
