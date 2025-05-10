import streamlit as st

def render_dashboard():
    def render_dashboard():

        import streamlit as st
        import json
        from pathlib import Path


        st.sidebar.title("🛡️ TA Category: Prompt Safety")
        assistant = st.sidebar.radio("Choose Assistant", ["TA-007v2: Instruction Firewall"])

        FIREWALL_PATH = Path("./ta-registry/TA-007/firewall_rules.json")
        FIREWALL_PATH.parent.mkdir(parents=True, exist_ok=True)
        if not FIREWALL_PATH.exists():
            default_rules = {"blocked_phrases": ["delete all", "sudo", "access client_db"]}
            FIREWALL_PATH.write_text(json.dumps(default_rules, indent=2))

        rules = json.load(open(FIREWALL_PATH))

        if assistant == "TA-007v2: Instruction Firewall":
            st.title("🛡️ TA-007 (v2): Firewall with Dynamic Rules")

            st.markdown("### 📝 Instruction Prompt to Scan")
            prompt = st.text_area("Paste compiled instruction or task")

            st.markdown("### 🔒 Active Firewall Rules")
            st.json(rules)

            if st.button("🧠 Scan for Violations"):
                hits = [term for term in rules["blocked_phrases"] if term.lower() in prompt.lower()]
                if hits:
                    st.error(f"❌ Violations: {', '.join(hits)}")
                else:
                    st.success("✅ No violations found.")