
import streamlit as st
from pathlib import Path
import json
from datetime import datetime

st.set_page_config(page_title="TA-049v2: Snapshot Viewer", layout="wide")

st.sidebar.title("📦 TA Category: Vector Snapshots")
assistant = st.sidebar.radio("Choose Assistant", ["TA-049v2: Archive Diff"])

snapshot_dir = Path("./ta-registry/TA-049/snapshots/")
snapshot_dir.mkdir(parents=True, exist_ok=True)

# Simulate two versions
current_snapshot = snapshot_dir / "snapshot_latest.json"
previous_snapshot = snapshot_dir / "snapshot_old.json"

# Write example data if not present
if not current_snapshot.exists():
    current_snapshot.write_text(json.dumps({"A": 0.91, "B": 0.72, "C": 0.86}, indent=2))
if not previous_snapshot.exists():
    previous_snapshot.write_text(json.dumps({"A": 0.90, "B": 0.73, "C": 0.80}, indent=2))

if assistant == "TA-049v2: Archive Diff":
    st.title("📦 TA-049 (v2): Snapshot Diff Viewer")

    if st.button("📸 Compare Snapshots"):
        snap_new = json.load(open(current_snapshot))
        snap_old = json.load(open(previous_snapshot))
        delta = {k: round(snap_new[k] - snap_old[k], 3) for k in snap_new if k in snap_old}
        st.markdown("### 🔍 Snapshot Delta")
        st.json(delta)

    st.markdown("### 📁 Latest Snapshot")
    st.code(current_snapshot.read_text())

    st.markdown("### 📁 Previous Snapshot")
    st.code(previous_snapshot.read_text())
