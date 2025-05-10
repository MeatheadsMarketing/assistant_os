
import streamlit as st
from pathlib import Path
import json

st.set_page_config(page_title="TA-004v2: Memory Injector", layout="wide")

st.sidebar.title("🧠 TA Category: Memory Injection")
assistant = st.sidebar.radio("Choose Assistant", ["TA-004v2: Memory Editor"])

if assistant == "TA-004v2: Memory Editor":
    st.title("🧠 TA-004 (v2): Memory Editor with Key Tagging")

    mem_path = Path("./ta-registry/TA-004/memory.json")
    mem_path.parent.mkdir(parents=True, exist_ok=True)
    if not mem_path.exists():
        mem_path.write_text(json.dumps({"client_name": "ACME Corp", "project_phase": "alpha"}, indent=2))

    memory = json.load(open(mem_path))
    st.markdown("### Current Memory Values")
    for key, value in memory.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.text(f"{key}: {value}")
        with col2:
            tag = st.radio(f"Tag: {key}", ["static", "volatile"], horizontal=True, key=key)

    if st.button("💾 Save Tagged Memory"):
        json.dump(memory, open(mem_path, "w"), indent=2)
        st.success("Memory saved.")
