
import streamlit as st

st.set_page_config(page_title="Assistant OS – Phase 8 (TA-101 to TA-105)", layout="wide")

st.sidebar.title("🛡️ TA Phase 8: Adversarial Intelligence")
tab = st.sidebar.radio("Choose Assistant", [
    "TA-101: Prompt Exploit Simulator",
    "TA-102: Role-Swap Adversary Arena",
    "TA-103: Red-Team Prompt Harness",
    "TA-104: GPT Self-Simulation Chamber",
    "TA-105: Shadow Prompt Detector"
])

if tab == "TA-101: Prompt Exploit Simulator":
    st.title("🛠️ TA-101: Prompt Exploit Simulator")
    st.markdown("Simulates known adversarial prompt variants against LLMs.")

elif tab == "TA-102: Role-Swap Adversary Arena":
    st.title("🤺 TA-102: Role-Swap Arena")
    st.markdown("Runs attacker/defender/judge roles using multi-agent architecture.")

elif tab == "TA-103: Red-Team Prompt Harness":
    st.title("🧪 TA-103: Prompt Harness")
    st.markdown("Injects prompts from a bank of known exploits.")

elif tab == "TA-104: GPT Self-Simulation Chamber":
    st.title("🧠 TA-104: Self-Simulation Chamber")
    st.markdown("Engages a GPT model to self-critique and revise its own outputs.")

elif tab == "TA-105: Shadow Prompt Detector":
    st.title("🕵️ TA-105: Shadow Prompt Detector")
    st.markdown("Scans prompt for stealth logic, framing traps, or jailbreak signatures.")
