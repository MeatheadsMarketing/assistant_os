import streamlit as st

def render_dashboard():
    def render_dashboard():

        import streamlit as st
        import re


        st.sidebar.title("🧼 TA Category: Context Hygiene")
        assistant = st.sidebar.radio("Choose Assistant", ["TA-045v2: Injection Cleaner"])

        if assistant == "TA-045v2: Injection Cleaner":
            st.title("🧼 TA-045 (v2): Clean Context for Injection Safety")

            raw_context = st.text_area("Paste Retrieved Context")

            def clean_context(text):
                # Remove user prompt patterns or meta injection
                patterns = [
                    r"(?i)user:.*",         # user statements
                    r"(?i)ignore previous.*",  # common jailbreaks
                    r"(?i)assistant:",      # model identifiers
                    r"(?i)as an ai model.*"
                ]
                for pat in patterns:
                    text = re.sub(pat, '', text)
                return text.strip()

            if st.button("🧹 Clean Context"):
                cleaned = clean_context(raw_context)
                st.subheader("🧠 Cleaned Context")
                st.code(cleaned)