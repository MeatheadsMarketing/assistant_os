
import streamlit as st
import pandas as pd
from pathlib import Path
import subprocess
import os

st.set_page_config(page_title="Assistant OS: Starter Suite", layout="wide")

st.sidebar.title("🧠 TA Starter Suite")
tab = st.sidebar.radio("Choose Assistant", ["TA-001: Instruction Diff", "TA-002: Version Tracker", "TA-003: Prompt Templater"])

# TA-001: Instruction Diff
if tab == "TA-001: Instruction Diff":
    st.title("🧠 TA-001: Instruction Diff Viewer")

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
            st.warning("No diff result found.")
    elif run_diff:
        st.error("Please upload both old and new instruction files.")

# TA-002: Version Tracker
elif tab == "TA-002: Version Tracker":
    st.title("🆕 TA-002: Instruction Version Tracker")

    uploaded_file = st.file_uploader("📁 Upload Instruction File", type="md")
    version_tag = st.text_input("🔖 Version (e.g., v1.4.2)")
    commit_message = st.text_area("✍️ Commit Message")

    run_track = st.button("📌 Track Version")

    if run_track and uploaded_file and version_tag and commit_message:
        version_path = Path(f"/tmp/{version_tag}.md")
        with open(version_path, "wb") as f:
            f.write(uploaded_file.read())

        commit_path = Path("./ta-registry/TA-002/changelog.md")
        with open(commit_path, "a") as f:
            f.write(f"## {version_tag}\n{commit_message}\n\n")

        st.success(f"Version {version_tag} logged.")
    elif run_track:
        st.warning("All fields are required.")

# TA-003: Prompt Templater
elif tab == "TA-003: Prompt Templater":
    st.title("🧩 TA-003: Prompt Templater")

    col1, col2 = st.columns(2)

    with col1:
        shared_file = st.file_uploader("📁 Upload Shared Logic File", type="md", key="shared")

    with col2:
        role_file = st.file_uploader("📁 Upload Role-Specific Logic File", type="md", key="role")

    merge = st.button("🧠 Merge Prompt")

    if merge and shared_file and role_file:
        shared_text = shared_file.read().decode("utf-8")
        role_text = role_file.read().decode("utf-8")

        final_prompt = f"""### SHARED RULES\n{shared_text}\n\n### ROLE RULES\n{role_text}"""
        st.subheader("📋 Final Prompt")
        st.code(final_prompt)
        st.download_button("📥 Download Prompt", data=final_prompt, file_name="final_prompt.md")
    elif merge:
        st.warning("Please upload both files.")
