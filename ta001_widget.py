
import streamlit as st
from pathlib import Path
import subprocess

st.set_page_config(page_title="TA-001: Instruction Diff", layout="wide")

# Sidebar toggle group for category
st.sidebar.title("🧠 TA Category: Instruction Stack")
assistant = st.sidebar.radio("Choose Assistant", ["TA-001: Instruction Diff"])

# UI for TA-001
if assistant == "TA-001: Instruction Diff":
    st.title("🧠 TA-001: Instruction Diff Viewer")

    st.markdown("This assistant compares two instruction files and shows behavioral diffs.")

    col1, col2 = st.columns(2)

    with col1:
        old_file = st.file_uploader("📁 Upload Old Instruction File", type="md", key="old")

    with col2:
        new_file = st.file_uploader("📁 Upload New Instruction File", type="md", key="new")

    run_diff = st.button("🧠 Run TA-001 Instruction Diff")

    if run_diff and old_file and new_file:
        old_path = Path("/tmp/old_instruction.md")
        new_path = Path("/tmp/new_instruction.md")
        with open(old_path, "wb") as f:
            f.write(old_file.read())
        with open(new_path, "wb") as f:
            f.write(new_file.read())

        # Save paths to ta-registry
        subprocess.run([
            "bash", "./ta-registry/TA-001/ta001_instruction_diff.sh",
            str(old_path), str(new_path)
        ])

        diff_output_path = Path("./ta-registry/TA-001/last_diff.md")
        if diff_output_path.exists():
            st.subheader("📝 Diff Result")
            with open(diff_output_path) as f:
                st.code(f.read())
        else:
            st.warning("No diff result found. Did the script run?")
    elif run_diff:
        st.error("Please upload both old and new instruction files before running.")
