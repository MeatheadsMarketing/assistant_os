
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="TA-027v2: Token Heatmap", layout="wide")

st.sidebar.title("🌡️ TA Category: Token Diagnostics")
assistant = st.sidebar.radio("Choose Assistant", ["TA-027v2: Token Heatmap Visual"])

if assistant == "TA-027v2: Token Heatmap Visual":
    st.title("🌡️ TA-027 (v2): Token Usage Heatmap")

    st.markdown("Enter content in each assistant section to compute token distribution.")

    sections = {
        "Prompt": st.text_area("📜 Prompt Block"),
        "Memory": st.text_area("🧠 Memory Block"),
        "Tool Call": st.text_area("🔧 Tool Call Block"),
        "Output": st.text_area("📝 Output Block")
    }

    if st.button("📊 Show Token Heatmap"):
        token_counts = {k: len(v.split()) for k, v in sections.items()}

        st.markdown("### 🔢 Token Count by Section")
        st.json(token_counts)

        # Plot as bar chart
        fig, ax = plt.subplots()
        ax.bar(token_counts.keys(), token_counts.values(), color="#7FDBFF")
        ax.set_ylabel("Tokens")
        ax.set_title("Token Distribution")
        st.pyplot(fig)
