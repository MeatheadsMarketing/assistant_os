
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="TA-003v3: Prompt Templater + Log Viewer", layout="wide")

st.sidebar.title("📚 TA Category: Prompt Templating")
assistant = st.sidebar.radio("Choose Assistant", ["TA-003v3: Prompt Builder + History"])

LOG_PATH = Path("./ta-registry/TA-003/prompt_history.log")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
if not LOG_PATH.exists():
    LOG_PATH.write_text("")

if assistant == "TA-003v3: Prompt Builder + History":
    st.title("📚 TA-003 (v3): Prompt Builder + Sidebar Log Viewer")

    shared_file = st.file_uploader("📁 Upload Shared Logic (.md)", type="md", key="shared")
    role_file = st.file_uploader("📁 Upload Role Logic (.md)", type="md", key="role")

    if shared_file and role_file:
        shared_text = shared_file.read().decode("utf-8")
        role_text = role_file.read().decode("utf-8")

        final_prompt = f"""### SHARED RULES\n{shared_text}\n\n### ROLE RULES\n{role_text}"""
        st.subheader("📋 Final Prompt")
        st.code(final_prompt)

        st.download_button("📥 Download Prompt", data=final_prompt, file_name="final_prompt.md")
        if st.button("📋 Copy Prompt (log to file)"):
            with open(LOG_PATH, "a") as f:
                f.write(final_prompt + "\n---\n")
            st.success("Prompt copied + logged to prompt_history.log")

    with st.sidebar:
        st.markdown("### 🕒 Recent Prompts")
        st.code(LOG_PATH.read_text()[-1000:] if LOG_PATH.exists() else "No logs found.")
