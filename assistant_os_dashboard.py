import streamlit as st
import pandas as pd
from pathlib import Path
import os
import subprocess

st.set_page_config(page_title="Assistant OS Dashboard", layout="wide")

tab = st.sidebar.radio("Go to", ["📄 Cover Page", "📊 Status Dashboard", "📝 Memory Editor", "📚 TA Browser", "📈 TA Health (TA-099 + TA-100)"])

# Cover Page
if tab == "📄 Cover Page":
    st.title("🧠 Assistant OS – TA Registry")
    st.markdown("## Contents")
    st.markdown("- 📊 Status Dashboard")
    st.markdown("- 📝 Memory Editor")
    st.markdown("- 📚 TA Browser")
    st.markdown("- 📈 TA Health (TA-099 + TA-100)")

# Status Dashboard
elif tab == "📊 Status Dashboard":
    st.title("📊 Build Status")
    try:
        df = pd.read_csv("ta_catalog.csv")
        df["Status"] = df.apply(lambda row: "✅ built" if os.path.exists(f"./ta-registry/{row['TA_ID']}/{row['CLI_File']}") else "❌ missing", axis=1)
        st.dataframe(df)
    except FileNotFoundError:
        st.warning("ta_catalog.csv not found in root directory.")

# Memory Editor
elif tab == "📝 Memory Editor":
    st.title("🧠 Memory Editor")
    mem_files = list(Path("./ta-registry").rglob("memory.json"))
    selected = st.selectbox("Select memory.json to edit", mem_files)
    if selected:
        content = Path(selected).read_text()
        edited = st.text_area("Edit memory.json", content, height=400)
        if st.button("💾 Save"):
            Path(selected).write_text(edited)
            st.success("File saved.")

# TA Catalog
elif tab == "📚 TA Browser":
    st.title("📚 TA Catalog")
    try:
        df = pd.read_csv("ta_catalog.csv")
        st.dataframe(df)
    except FileNotFoundError:
        st.warning("ta_catalog.csv is missing. Please ensure it's in the root directory.")

# TA Health
elif tab == "📈 TA Health (TA-099 + TA-100)":
    st.title("📈 TA Registry Health")
    if st.button("Run TA-099"):
        subprocess.run(["bash", "./ta-registry/ta099_evaluate_assistant_os.sh"])
    if st.button("Run TA-100"):
        subprocess.run(["bash", "./ta-registry/ta100_run_auto_evolve.sh"])

    if os.path.exists("./ta-registry/meta_scorecard.md"):
        with open("./ta-registry/meta_scorecard.md") as f:
            st.markdown(f.read())
    else:
        st.warning("TA-099 output file not found.")

    if os.path.exists("./ta-registry/proposed_updates.json"):
        with open("./ta-registry/proposed_updates.json") as f:
            st.json(f.read())
    else:
        st.warning("TA-100 suggestions file not found.")
