import streamlit as st

def render_dashboard():
    def render_dashboard():

        import streamlit as st


        st.sidebar.title("🧠 TA Category: Context Injection Analysis")
        assistant = st.sidebar.radio("Choose Assistant", ["TA-050v2: Injection Comparator"])

        if assistant == "TA-050v2: Injection Comparator":
            st.title("🧠 TA-050 (v2): With vs. Without Context")

            col1, col2 = st.columns(2)

            with col1:
                with_ctx = st.text_area("🧩 Output WITH Context", height=200)
            with col2:
                without_ctx = st.text_area("🧩 Output WITHOUT Context", height=200)

            if st.button("📊 Evaluate Impact"):
                score = abs(len(with_ctx.strip()) - len(without_ctx.strip()))
                verdict = "context improved output" if score > 15 else "context had minimal impact"
                st.success(f"Verdict: {verdict} (Token delta: {score})")
                st.markdown("### 📋 Diff Preview")
                st.code(f"- With: {with_ctx.strip()}\n\n- Without: {without_ctx.strip()}")