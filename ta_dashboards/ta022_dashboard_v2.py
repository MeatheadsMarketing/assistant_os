
import streamlit as st

st.set_page_config(page_title="TA-022v2: Token Budget Enforcer", layout="wide")

st.sidebar.title("🔢 TA Category: Token Safety")
assistant = st.sidebar.radio("Choose Assistant", ["TA-022v2: Token Limit Checker"])

if assistant == "TA-022v2: Token Limit Checker":
    st.title("🔢 TA-022 (v2): Token Budget + Strict Mode")

    text = st.text_area("📄 Paste Assistant Output")
    limit = st.slider("🧮 Token Limit", min_value=50, max_value=2048, value=300)
    strict = st.checkbox("⚠️ Strict Mode (hard block)")

    if st.button("🔍 Check Token Usage"):
        count = len(text.split())
        if count > limit:
            if strict:
                st.error(f"❌ {count} tokens exceeds limit. Strict Mode = BLOCKED.")
            else:
                st.warning(f"⚠️ {count} tokens exceeds limit.")
        else:
            st.success(f"✅ Output within limit ({count}/{limit} tokens).")
