import streamlit as st

def render_dashboard():
    def render_dashboard():

        import streamlit as st
        import random


        st.sidebar.title("📝 TA Category: Feedback & Scoring")
        assistant = st.sidebar.radio("Choose Assistant", ["TA-094v2: Rubric Scorer"])

        if assistant == "TA-094v2: Rubric Scorer":
            st.title("📝 TA-094 (v2): Feedback Scorer with Rubric")

            feedback = st.text_area("Paste Feedback")
            rubric = st.multiselect("Select Scoring Criteria", ["Clarity", "Accuracy", "Tone", "Helpfulness", "Usefulness"])

            if st.button("📊 Score Feedback"):
                scores = {r: random.randint(60, 100) for r in rubric}
                if scores:
                    st.markdown("### 🧾 Scored Result")
                    st.json(scores)
                    st.success(f"Average Score: {sum(scores.values()) // len(scores)}")
                else:
                    st.warning("Select at least one rubric.")