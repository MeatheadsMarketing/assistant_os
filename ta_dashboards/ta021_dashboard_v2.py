
import streamlit as st
import json
import matplotlib.pyplot as plt

st.set_page_config(page_title="TA-021v2: Schema Validator + Visual", layout="wide")

st.sidebar.title("📐 TA Category: JSON Validation")
assistant = st.sidebar.radio("Choose Assistant", ["TA-021v2: Schema Visualizer"])

if assistant == "TA-021v2: Schema Visualizer":
    st.title("📐 TA-021 (v2): JSON Schema Validator")

    json_input = st.text_area("📄 Paste Assistant Output (JSON)", height=200)
    strict = st.checkbox("⚠️ Strict Mode")

    if st.button("🧪 Validate JSON"):
        try:
            parsed = json.loads(json_input)
            fields = list(parsed.keys())
            st.success("✅ JSON parsed successfully.")
            st.markdown("### 🧬 Visualize Field Spread")

            fig, ax = plt.subplots()
            bars = [len(str(parsed[f])) for f in fields]
            ax.bar(fields, bars, color="#2ECC40")
            ax.set_ylabel("Value Length")
            ax.set_title("📊 Field Size by Key")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        except Exception as e:
            if strict:
                st.error(f"❌ Strict Mode: Validation failed. Reason: {e}")
            else:
                st.warning(f"⚠️ Soft Fail: Invalid JSON, but strict mode is off.")
