
import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="TA-004v3: Memory Editor + Compare", layout="wide")

st.sidebar.title("🧠 TA Category: Memory Injector")
assistant = st.sidebar.radio("Choose Assistant", ["TA-004v3: Memory Compare"])

mem_path = Path("./ta-registry/TA-004/memory.json")
mem_path.parent.mkdir(parents=True, exist_ok=True)
if not mem_path.exists():
    mem_path.write_text(json.dumps({"client_name": "ACME Corp"}, indent=2))

# Load reference memory from another TA
all_mem_files = list(Path("./ta-registry").rglob("memory.json"))
compare_mem = st.sidebar.selectbox("🔄 Compare with another TA", all_mem_files)

if assistant == "TA-004v3: Memory Compare":
    st.title("🧠 TA-004 (v3): Memory Editor + Cross-TA Compare")

    memory = json.load(open(mem_path))
    st.markdown("### Current Memory (Editable)")
    edited = st.json(memory)

    if st.button("💾 Save Memory"):
        json.dump(edited, open(mem_path, "w"), indent=2)
        st.success("Memory saved.")

    if compare_mem:
        st.markdown(f"### Comparison with: `{compare_mem.name}`")
        try:
            other_mem = json.load(open(compare_mem))
            st.json(other_mem)
        except:
            st.warning("Could not parse comparison file.")
