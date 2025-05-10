
import streamlit as st
from pathlib import Path
import json

st.set_page_config(page_title="TA-020v2: Permission-Safe Injector", layout="wide")

st.sidebar.title("🔐 TA Category: Access Control")
assistant = st.sidebar.radio("Choose Assistant", ["TA-020v2: Permission Matrix"])

perm_file = Path("./ta-registry/TA-020/access_rules.json")
perm_file.parent.mkdir(parents=True, exist_ok=True)

# Initialize default access rules
if not perm_file.exists():
    perm_file.write_text(json.dumps({
        "SummarizerGPT": ["summary_limit", "client_tone"],
        "PlannerGPT": ["meeting_window", "calendar_slots"],
        "MemoryGPT": ["retention_policy", "embedding_space"]
    }, indent=2))

rules = json.load(open(perm_file))

if assistant == "TA-020v2: Permission Matrix":
    st.title("🔐 TA-020 (v2): Scoped Memory Access")

    st.markdown("### 🔎 Visual Role-Memory Access Matrix")
    for role, keys in rules.items():
        st.markdown(f"**{role}** → {', '.join(keys)}")

    st.markdown("---")
    st.markdown("### 🧠 Validate Memory Key Access")

    role = st.selectbox("Role", list(rules.keys()))
    key = st.text_input("Memory Key to Inject")

    if st.button("✅ Check Permission"):
        if key in rules[role]:
            st.success(f"✅ {role} is allowed to write `{key}`")
        else:
            st.error(f"❌ {role} is NOT authorized to access `{key}`")
