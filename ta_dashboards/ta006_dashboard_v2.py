
import streamlit as st

st.set_page_config(page_title="TA-006v2: Output Validator", layout="wide")

st.sidebar.title("🧪 TA Category: Output Validation")
assistant = st.sidebar.radio("Choose Assistant", ["TA-006v2: Structured Validator"])

if assistant == "TA-006v2: Structured Validator":
    st.title("📋 TA-006 (v2): Output Quality Validator")

    st.markdown("### ✍️ Paste Assistant Output")
    output = st.text_area("Response to Validate")

    st.markdown("### ⚙️ Select Validation Checks")
    structure = st.checkbox("✅ Structure / JSON validity")
    tone = st.checkbox("🧠 Tone & Clarity")
    safety = st.checkbox("🚫 Safety / Dangerous content")

    if st.button("🔍 Validate Output"):
        if not output:
            st.warning("Paste output to validate.")
        else:
            if structure and not output.strip().startswith("{"):
                st.error("❌ Structure check failed: Not JSON-like.")
            elif structure:
                st.success("✅ Structure looks valid.")

            if tone and any(term in output.lower() for term in ["uh", "maybe", "kind of"]):
                st.warning("⚠️ Tone check: Uncertain or soft language detected.")
            elif tone:
                st.success("✅ Tone: Confident.")

            if safety and any(term in output.lower() for term in ["drop", "delete", "sudo"]):
                st.error("❌ Safety check failed: Dangerous command terms.")
            elif safety:
                st.success("✅ Safe.")
