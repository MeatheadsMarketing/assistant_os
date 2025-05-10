
import streamlit as st
from pathlib import Path
import subprocess

st.set_page_config(page_title="TA-002: Version Tracker", layout="wide")

st.sidebar.title("🧠 TA Category: Instruction Stack")
assistant = st.sidebar.radio("Choose Assistant", ["TA-002: Version Tracker"])

if assistant == "TA-002: Version Tracker":
    st.title("🆕 TA-002: Instruction Version Tracker")

    st.markdown("Upload an instruction file, tag it with a version, and append a commit log.")

    uploaded_file = st.file_uploader("📁 Upload Instruction File", type="md")
    version_tag = st.text_input("🔖 Version (e.g., v1.4.2)")
    commit_message = st.text_area("✍️ Commit Message")

    run_track = st.button("📌 Track Version")

    if run_track and uploaded_file and version_tag and commit_message:
        version_path = Path(f"/tmp/{version_tag}.md")
        with open(version_path, "wb") as f:
            f.write(uploaded_file.read())

        # Save commit message
        commit_path = Path("./ta-registry/TA-002/changelog.md")
        with open(commit_path, "a") as f:
            f.write(f"## {version_tag}\n{commit_message}\n\n")

        st.success(f"Version {version_tag} logged with commit.")
    elif run_track:
        st.warning("All fields are required.")
