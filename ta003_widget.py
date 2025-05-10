
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="TA-003: Prompt Templater", layout="wide")

st.sidebar.title("🧠 TA Category: Instruction Stack")
assistant = st.sidebar.radio("Choose Assistant", ["TA-003: Prompt Templater"])

if assistant == "TA-003: Prompt Templater":
    st.title("🧩 TA-003: Prompt Templater")

    st.markdown("Upload shared and role-specific logic blocks to assemble a complete assistant prompt.")

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
        st.warning("Please upload both files before merging.")
