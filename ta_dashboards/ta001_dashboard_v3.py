
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="TA-001v3: Instruction Diff", layout="wide")

st.sidebar.title("🧠 TA Category: Instruction Stack")
assistant = st.sidebar.radio("Choose Assistant", ["TA-001v3: Synced Diff Viewer"])

if assistant == "TA-001v3: Synced Diff Viewer":
    st.title("🧠 TA-001 (v3): Dual Instruction Diff Viewer")

    col1, col2 = st.columns(2)
    with col1:
        old_file = st.file_uploader("📁 Upload OLD Instruction (.md)", type="md", key="old_v3")
        if old_file:
            old_text = old_file.read().decode("utf-8")
            st.text_area("📜 OLD Instruction", value=old_text, height=400)

    with col2:
        new_file = st.file_uploader("📁 Upload NEW Instruction (.md)", type="md", key="new_v3")
        if new_file:
            new_text = new_file.read().decode("utf-8")
            st.text_area("📘 NEW Instruction", value=new_text, height=400)

    if old_file and new_file and st.button("🔍 Show Inline Diff"):
        import difflib
        old_lines = old_text.splitlines()
        new_lines = new_text.splitlines()
        diff = list(difflib.unified_diff(old_lines, new_lines, lineterm=""))

        st.markdown("### 🧾 Diff Output")
        for line in diff:
            if line.startswith("+") and not line.startswith("+++"):
                st.markdown(f"<span style='color:green'>{line}</span>", unsafe_allow_html=True)
            elif line.startswith("-") and not line.startswith("---"):
                st.markdown(f"<span style='color:red'>{line}</span>", unsafe_allow_html=True)
            else:
                st.code(line)
