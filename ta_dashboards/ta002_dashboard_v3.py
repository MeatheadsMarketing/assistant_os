
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="TA-002v3: Version Tracker + Auto Detection", layout="wide")

st.sidebar.title("🆕 TA Category: Versioning")
assistant = st.sidebar.radio("Choose Assistant", ["TA-002v3: Auto Detect Mode"])

CHANGELOG = Path("./ta-registry/TA-002/changelog.md")
CHANGELOG.parent.mkdir(parents=True, exist_ok=True)

if assistant == "TA-002v3: Auto Detect Mode":
    st.title("🆕 TA-002 (v3): Version Tracker + Auto-Type Detection")

    uploaded = st.file_uploader("📁 Upload Instruction File", type="md")
    autodetect = st.checkbox("🧠 Auto-detect Instruction Type")
    instruction_type = "System Prompt"  # default fallback

    if uploaded and autodetect:
        content = uploaded.read().decode("utf-8")
        if "summarize" in content.lower():
            instruction_type = "Summarizer"
        elif "calendar" in content.lower():
            instruction_type = "Planner"
        elif "extract" in content.lower():
            instruction_type = "Fact Extractor"
        else:
            instruction_type = "General Logic"

        st.success(f"🔍 Detected Instruction Type: **{instruction_type}**")
        st.text_area("Instruction Preview", content, height=300)

    tag = st.text_input("🔖 Version Tag")
    note = st.text_area("📝 Commit Message")

    if st.button("💾 Commit Version"):
        if uploaded and tag and note:
            entry = f"## {tag}\nType: {instruction_type}\n{note}\n\n"
            with open(CHANGELOG, "a") as f:
                f.write(entry)
            st.success(f"✅ {tag} committed to changelog.")
        else:
            st.error("Please complete all fields before committing.")
