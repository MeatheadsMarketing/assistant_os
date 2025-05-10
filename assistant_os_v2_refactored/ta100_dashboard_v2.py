import streamlit as st

def render_dashboard():
    def render_dashboard():

        import streamlit as st
        import json
        from pathlib import Path
        from datetime import datetime


        st.sidebar.title("♻️ TA Category: Self-Evolution")
        assistant = st.sidebar.radio("Choose Assistant", ["TA-100v2: Evolution History"])

        log_path = Path("./ta-registry/TA-100/proposed_updates.json")
        log_path.parent.mkdir(parents=True, exist_ok=True)
        if not log_path.exists():
            log_path.write_text("[]")

        if assistant == "TA-100v2: Evolution History":
            st.title("♻️ TA-100 (v2): Auto-Evolution Tracker")

            st.markdown("### 📝 Suggest an Upgrade")
            ta_id = st.text_input("TA ID to Improve")
            suggestion = st.text_area("Upgrade Suggestion")
            priority = st.selectbox("Priority", ["High", "Medium", "Low"])

            if st.button("💾 Add Suggestion"):
                history = json.load(open(log_path))
                history.append({
                    "timestamp": datetime.now().isoformat(),
                    "ta_id": ta_id,
                    "suggestion": suggestion,
                    "priority": priority
                })
                json.dump(history, open(log_path, "w"), indent=2)
                st.success("✅ Logged.")

            st.markdown("### 📋 Suggestion History")
            st.json(json.load(open(log_path)))