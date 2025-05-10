
import streamlit as st

st.set_page_config(page_title="TA-061v2: Self-Reflection Engine", layout="wide")

st.sidebar.title("🧠 TA Category: Reflection + Rewrite")
assistant = st.sidebar.radio("Choose Assistant", ["TA-061v2: Self-Reflection + Rewrite"])

if assistant == "TA-061v2: Self-Reflection + Rewrite":
    st.title("💭 TA-061 (v2): Reflect + Rewrite")

    original = st.text_area("📄 Original Assistant Output", height=200)

    if st.button("🧠 Reflect"):
        word_count = len(original.split())
        st.markdown(f"📝 Reflection: This response is **{word_count} tokens** long. Consider reducing verbosity or increasing precision.")

    st.markdown("### ✍️ Optional Rewrite")
    rewrite = st.text_area("🔁 Rewritten Output", height=200)
    if st.button("💾 Save Rewrite"):
        st.success("Rewrite submitted (simulated).")
        st.code(rewrite)
