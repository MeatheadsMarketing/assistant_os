import streamlit as st

def render_dashboard():
    def render_dashboard():

        import streamlit as st
        import json
        from pathlib import Path


        st.sidebar.title("🧪 TA Category: Drift Detection")
        assistant = st.sidebar.radio("Choose Assistant", ["TA-025v2: Output Drift Logger"])

        log_path = Path("./ta-registry/TA-025/drift_log.json")
        log_path.parent.mkdir(parents=True, exist_ok=True)
        if not log_path.exists():
            log_path.write_text("[]")

        if assistant == "TA-025v2: Output Drift Logger":
            st.title("🔁 TA-025 (v2): Consistency Drift Logger")

            run_1 = st.text_area("Output Run 1")
            run_2 = st.text_area("Output Run 2")

            if st.button("📊 Compare & Log Drift"):
                drift = run_1.strip() != run_2.strip()
                record = {
                    "match": not drift,
                    "run_1": run_1.strip(),
                    "run_2": run_2.strip()
                }
                history = json.load(open(log_path))
                history.append(record)
                json.dump(history, open(log_path, "w"), indent=2)

                if drift:
                    st.warning("⚠️ Drift detected — outputs differ.")
                else:
                    st.success("✅ Outputs are consistent.")

            st.markdown("### 📁 Drift Log")
            st.json(json.load(open(log_path)))