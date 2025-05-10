
import streamlit as st
import json
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="TA-084v2: Deployment Pinner", layout="wide")

st.sidebar.title("📌 TA Category: Deployment Versioning")
assistant = st.sidebar.radio("Choose Assistant", ["TA-084v2: Version Pinning"])

pin_path = Path("./ta-registry/TA-084/pinned_versions.json")
pin_path.parent.mkdir(parents=True, exist_ok=True)
if not pin_path.exists():
    pin_path.write_text("[]")

if assistant == "TA-084v2: Version Pinning":
    st.title("📌 TA-084 (v2): Deployment Version Tracker")

    assistant_id = st.text_input("Assistant ID (e.g., TA-004)")
    version = st.text_input("Version (e.g., v1.3.2)")
    env = st.selectbox("Environment", ["staging", "production", "qa"])

    if st.button("✅ Pin Version"):
        log = json.load(open(pin_path))
        log.append({
            "assistant_id": assistant_id,
            "version": version,
            "environment": env,
            "timestamp": datetime.now().isoformat()
        })
        json.dump(log, open(pin_path, "w"), indent=2)
        st.success(f"Pinned {version} for {assistant_id} → {env}")

    st.markdown("### 📋 Pinned Versions Log")
    st.json(json.load(open(pin_path)))
