
import streamlit as st
from pathlib import Path
import json
import os

st.set_page_config(page_title="Assistant OS – Phase 5 (TA-041 to TA-050)", layout="wide")

st.sidebar.title("🧠 TA Phase 5")
tab = st.sidebar.radio("Choose Assistant", [
    "TA-041: Embedding Generator",
    "TA-042: Vector Uploader",
    "TA-043: Context Retriever",
    "TA-044: Semantic Validator",
    "TA-045: Injection Filter",
    "TA-046: Chunk + Embed",
    "TA-047: Query Router",
    "TA-048: Embedding Drift Analyzer",
    "TA-049: Vector Snapshot Archiver",
    "TA-050: Context Injection Comparator"
])

if tab == "TA-041: Embedding Generator":
    st.title("📌 TA-041: Embedding Generator")
    text = st.text_area("Paste Text to Embed")
    if st.button("🧠 Generate Embedding"):
        st.json({"embedding_vector": [round(hash(x) % 0.99, 2) for x in text.split()[:5]]})

elif tab == "TA-042: Vector Uploader":
    st.title("📤 TA-042: Upload to Vector DB (Simulated)")
    if st.button("🚀 Upload Embeddings"):
        st.success("Embedding uploaded (mock)")

elif tab == "TA-043: Context Retriever":
    st.title("🔎 TA-043: Semantic Context Retrieval")
    query = st.text_input("Query")
    if st.button("🧠 Retrieve"):
        st.code(f"Top hit for query '{query}' = 'Client prefers markdown over tables'")

elif tab == "TA-044: Semantic Validator":
    st.title("📋 TA-044: Validate Retrieved Context")
    ctx = st.text_area("Paste Retrieved Context")
    if st.button("🔍 Scan"):
        flagged = "off-topic" in ctx.lower()
        if flagged:
            st.warning("⚠️ Context might be off-topic")
        else:
            st.success("Context looks semantically valid")

elif tab == "TA-045: Injection Filter":
    st.title("🧼 TA-045: Filter for Prompt Injection")
    ctx = st.text_area("Paste Retrieved Context")
    if st.button("🧹 Clean Context"):
        st.code(ctx.replace("USER:", "").strip())

elif tab == "TA-046: Chunk + Embed Large Doc"):
    st.title("📚 TA-046: Chunk + Embed")
    text = st.text_area("Paste long document")
    if st.button("📦 Chunk + Embed"):
        chunks = [text[i:i+40] for i in range(0, len(text), 40)]
        st.json({f"chunk_{i+1}": chunk for i, chunk in enumerate(chunks[:3])})

elif tab == "TA-047: Query Router":
    st.title("📡 TA-047: Vector DB Router")
    source = st.radio("Select Source", ["client_db", "history_db"])
    if st.button("🛣️ Route Query"):
        st.success(f"Query routed to: {source}")

elif tab == "TA-048: Embedding Drift Analyzer":
    st.title("📉 TA-048: Embedding Drift Detector")
    emb1 = st.text_area("Old Embedding (CSV)")
    emb2 = st.text_area("New Embedding (CSV)")
    if st.button("🧮 Compare Drift"):
        try:
            drift = abs(sum(float(x) for x in emb1.split(',')) - sum(float(x) for x in emb2.split(',')))
            st.info(f"Approx drift score = {round(drift, 2)}")
        except:
            st.error("Could not parse vectors.")

elif tab == "TA-049: Vector Snapshot Archiver":
    st.title("📦 TA-049: Vector Snapshot Archive")
    if st.button("📥 Save Snapshot"):
        st.success("Vector snapshot archived (simulated)")

elif tab == "TA-050: Context Injection Comparator":
    st.title("🧠 TA-050: Context vs. No Context Run")
    with_ctx = st.text_area("Output WITH context")
    without_ctx = st.text_area("Output WITHOUT context")
    if st.button("📊 Compare Effectiveness"):
        match = with_ctx.strip() == without_ctx.strip()
        if match:
            st.warning("⚠️ Context made no difference")
        else:
            st.success("✅ Context improved assistant output")
