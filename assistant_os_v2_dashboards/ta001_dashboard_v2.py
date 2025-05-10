
import streamlit as st
from pathlib import Path
import difflib

st.set_page_config(page_title="TA-001v2: Instruction Diff Viewer", layout="wide")

st.sidebar.title("🧠 TA Category: Instruction Stack")
assistant = st.sidebar.radio("Choose Assistant", ["TA-001v2: Instruction Diff"])

if assistant == "TA-001v2: Instruction Diff":
    st.title("🧠 TA-001 (v2): Side-by-Side Diff Viewer")

    col1, col2 = st.columns(2)
    with col1:
        old_file = st.file_uploader("📁 Upload Old Instruction File", type="md", key="old_v2")
    with col2:
        new_file = st.file_uploader("📁 Upload New Instruction File", type="md", key="new_v2")

    if old_file and new_file:
        old_lines = old_file.read().decode("utf-8").splitlines()
        new_lines = new_file.read().decode("utf-8").splitlines()

        st.markdown("### 🔍 Diff Overview")
        diff = list(difflib.unified_diff(old_lines, new_lines, lineterm=""))
        if not diff:
            st.success("✅ No differences detected.")
        else:
            for line in diff:
                if line.startswith("+") and not line.startswith("+++"):
                    st.markdown(f"<span style='color:green'>{line}</span>", unsafe_allow_html=True)
                elif line.startswith("-") and not line.startswith("---"):
                    st.markdown(f"<span style='color:red'>{line}</span>", unsafe_allow_html=True)
                else:
                    st.code(line)
    else:
        st.info("Upload both old and new instruction files to see differences.")
