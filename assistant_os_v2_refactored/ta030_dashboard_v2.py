import streamlit as st

def render_dashboard():
    def render_dashboard():

        import streamlit as st


        st.sidebar.title("🚨 TA Category: Safety + Monitoring")
        assistant = st.sidebar.radio("Choose Assistant", ["TA-030v2: Anomaly Scanner"])

        if assistant == "TA-030v2: Anomaly Scanner":
            st.title("🚨 TA-030 (v2): Output Anomaly Detector")

            output = st.text_area("Paste assistant output")

            anomaly_terms = ["drop table", "sudo", "rm -rf", "panic", "hacked"]
            explanations = {
                "drop table": "⚠️ SQL injection risk detected.",
                "sudo": "⚠️ Privilege escalation keyword.",
                "rm -rf": "⚠️ Destructive system command.",
                "panic": "⚠️ Emotionally loaded or unstable tone.",
                "hacked": "⚠️ Suggests compromised behavior or context."
            }

            if st.button("🔍 Scan Output"):
                hits = [term for term in anomaly_terms if term in output.lower()]
                if hits:
                    st.error("❗ Anomaly Detected:")
                    for term in hits:
                        st.markdown(f"- `{term}` → {explanations[term]}")
                else:
                    st.success("✅ Output appears safe.")