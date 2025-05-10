
import streamlit as st

st.set_page_config(page_title="TA-005v2: Tool Invocation Gatekeeper", layout="wide")

st.sidebar.title("🛡️ TA Category: Tool Permissions")
assistant = st.sidebar.radio("Choose Assistant", ["TA-005v2: Tool Access Gatekeeper"])

if assistant == "TA-005v2: Tool Access Gatekeeper":
    st.title("🔐 TA-005 (v2): Tool Gatekeeper with Role Registry")

    tool = st.text_input("🧰 Tool Name (e.g., calendar_api)")
    st.markdown("### 🧠 Select Assistant Role")

    role_registry = {
        "SummarizerGPT": ["text_cleaner", "token_counter"],
        "PlannerGPT": ["calendar_api", "reminder_bot"],
        "MemoryGPT": ["memory_injector", "vector_search"]
    }

    selected_role = st.selectbox("Select Role", list(role_registry.keys()))

    if st.button("🔎 Check Access"):
        allowed_tools = role_registry[selected_role]
        if tool in allowed_tools:
            st.success(f"✅ {selected_role} is allowed to use `{tool}`.")
        else:
            st.error(f"🚫 {selected_role} is NOT allowed to use `{tool}`.")
