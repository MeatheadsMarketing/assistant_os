import streamlit as st

def render_dashboard():
    def render_dashboard():

        import streamlit as st
        from pathlib import Path


        st.sidebar.title("🧠 TA Category: Instruction Stack")
        assistant = st.sidebar.radio("Choose Assistant", ["TA-003v2: Prompt Templater"])

        if assistant == "TA-003v2: Prompt Templater":
            st.title("🧩 TA-003 (v2): Prompt Builder + Clipboard")

            col1, col2 = st.columns(2)
            with col1:
                shared_file = st.file_uploader("📁 Upload Shared Logic (.md)", type="md", key="shared_v2")
            with col2:
                role_file = st.file_uploader("📁 Upload Role Logic (.md)", type="md", key="role_v2")

            if shared_file and role_file:
                shared_text = shared_file.read().decode("utf-8")
                role_text = role_file.read().decode("utf-8")

                final_prompt = f"""### SHARED RULES\n{shared_text}\n\n### ROLE RULES\n{role_text}"""

                st.subheader("📋 Final Prompt")
                st.code(final_prompt)

                st.download_button("📥 Download Prompt", data=final_prompt, file_name="final_prompt.md")
                st.text("📋 Use Cmd/Ctrl+C to copy the prompt above manually.")
            else:
                st.info("Please upload both shared and role logic files.")