
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="TA-014v2: Fact Queue History", layout="wide")

st.sidebar.title("📥 TA Category: Memory Audit")
assistant = st.sidebar.radio("Choose Assistant", ["TA-014v2: Queue History Viewer"])

queue_path = Path("./ta-registry/TA-012/fact_queue.txt")
queue_path.parent.mkdir(parents=True, exist_ok=True)
if not queue_path.exists():
    queue_path.write_text("Preferred format: bullet list\nClient tone: assertive")

if assistant == "TA-014v2: Queue History Viewer":
    st.title("📥 TA-014 (v2): Fact Queue + History Viewer")

    st.markdown("### 📋 Current Queue Preview")
    facts = queue_path.read_text().strip().split("\n")
    if facts:
        st.code("\n".join(facts[-10:]))
    else:
        st.info("No facts queued yet.")

    if st.button("🧹 Clear Queue"):
        queue_path.write_text("")
        st.success("Queue cleared.")
