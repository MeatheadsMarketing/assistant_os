import streamlit as st

def render_dashboard():
    def render_dashboard():

        import streamlit as st


        st.sidebar.title("📉 TA Category: Embedding Drift")
        assistant = st.sidebar.radio("Choose Assistant", ["TA-048v2: Vector Drift Analyzer"])

        if assistant == "TA-048v2: Vector Drift Analyzer":
            st.title("📉 TA-048 (v2): Drift Analyzer")

            emb1 = st.text_area("Old Embedding Vector (comma-separated)", key="emb1")
            emb2 = st.text_area("New Embedding Vector (comma-separated)", key="emb2")

            if st.button("🧮 Analyze Drift"):
                try:
                    vec1 = [float(x.strip()) for x in emb1.split(",") if x.strip()]
                    vec2 = [float(x.strip()) for x in emb2.split(",") if x.strip()]
                    if len(vec1) != len(vec2):
                        st.error("Vectors must be the same length.")
                    else:
                        delta = [round(abs(a - b), 4) for a, b in zip(vec1, vec2)]
                        drift_score = round(sum(delta), 4)
                        st.success(f"Total Drift Score: {drift_score}")
                        st.json({"delta_per_dimension": delta})
                except Exception as e:
                    st.error(f"Parse error: {e}")