
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="TA-002v2: Version Tracker", layout="wide")

st.sidebar.title("🧠 TA Category: Instruction Stack")
assistant = st.sidebar.radio("Choose Assistant", ["TA-002v2: Version Tracker"])

CHANGELOG = Path("./ta-registry/TA-002/changelog.md")
CHANGELOG.parent.mkdir(parents=True, exist_ok=True)

if assistant == "TA-002v2: Version Tracker":
    st.title("🆕 TA-002 (v2): Instruction Version Tracker")

    st.markdown("### 🧾 Versioning Log")
    if CHANGELOG.exists():
        raw_log = CHANGELOG.read_text().split("## ")
        version_blocks = [entry.strip() for entry in raw_log if entry.strip()]
        version_labels = [block.split("\n")[0] for block in version_blocks]

        selected = st.selectbox("📜 View Previous Versions", version_labels)
        selected_block = [b for b in version_blocks if b.startswith(selected)][0]
        st.code(selected_block)

        if st.button("🛑 Roll Back to This Version"):
            rollback_path = Path(f"./ta-registry/TA-002/rollback_{selected}.md")
            rollback_path.write_text(selected_block)
            st.success(f"Rollback candidate saved as: {rollback_path.name}")
    else:
        st.warning("No changelog found. Submit a version first.")

    st.markdown("---")
    st.markdown("### 🆕 Submit New Version")
    new_file = st.file_uploader("📁 Upload Instruction File (.md)", type="md")
    tag = st.text_input("🔖 Version Tag (e.g., v1.2.0)")
    summary = st.text_area("✍️ Commit Summary")

    if st.button("💾 Commit Version"):
        if new_file and tag and summary:
            entry = f"## {tag}\n{summary}\n\n"
            with open(CHANGELOG, "a") as f:
                f.write(entry)
            st.success(f"✅ {tag} committed to changelog.")
        else:
            st.error("Please upload a file, add a tag, and write a summary.")
