
import streamlit as st

# Import refactored render_dashboard functions
from ta001_dashboard_v2 import render_dashboard as run_ta001
from ta002_dashboard_v2 import render_dashboard as run_ta002
from ta003_dashboard_v2 import render_dashboard as run_ta003
from ta004_dashboard_v2 import render_dashboard as run_ta004
from ta005_dashboard_v2 import render_dashboard as run_ta005
from ta006_dashboard_v2 import render_dashboard as run_ta006
from ta007_dashboard_v2 import render_dashboard as run_ta007
from ta012_dashboard_v2 import render_dashboard as run_ta012
from ta013_dashboard_v2 import render_dashboard as run_ta013
from ta020_dashboard_v2 import render_dashboard as run_ta020
from ta025_dashboard_v2 import render_dashboard as run_ta025
from ta027_dashboard_v2 import render_dashboard as run_ta027
from ta030_dashboard_v2 import render_dashboard as run_ta030
from ta045_dashboard_v2 import render_dashboard as run_ta045
from ta048_dashboard_v2 import render_dashboard as run_ta048
from ta050_dashboard_v2 import render_dashboard as run_ta050
from ta061_dashboard_v2 import render_dashboard as run_ta061
from ta065_dashboard_v2 import render_dashboard as run_ta065
from ta069_dashboard_v2 import render_dashboard as run_ta069
from ta084_dashboard_v2 import render_dashboard as run_ta084
from ta094_dashboard_v2 import render_dashboard as run_ta094
from ta100_dashboard_v2 import render_dashboard as run_ta100

st.set_page_config(page_title="Assistant OS – Merged UI", layout="wide")
st.title("🧠 Assistant OS – Phase Merger UI")

selection = st.sidebar.selectbox("📂 Jump to TA Module", [
    "TA-001 → TA-003: Instruction Stack",
    "TA-004 → TA-007: Memory + Access",
    "TA-012 → TA-013: Fact Queueing",
    "TA-020: Permission Matrix",
    "TA-025: Output Consistency",
    "TA-027: Token Heatmap",
    "TA-030: Anomaly Detector",
    "TA-045: Context Cleaner",
    "TA-048: Embedding Drift",
    "TA-050: Context Comparison",
    "TA-061: Reflection + Rewrite",
    "TA-065: Autonomy Logger",
    "TA-069: Agent Loop Map",
    "TA-084: Deployment Pinner",
    "TA-094: Feedback Rubric Scorer",
    "TA-100: Auto-Evolution Log"
])

# Route to dashboards
dashboard_map = {
    "TA-001 → TA-003: Instruction Stack": run_ta001,
    "TA-004 → TA-007: Memory + Access": run_ta004,
    "TA-012 → TA-013: Fact Queueing": run_ta012,
    "TA-020: Permission Matrix": run_ta020,
    "TA-025: Output Consistency": run_ta025,
    "TA-027: Token Heatmap": run_ta027,
    "TA-030: Anomaly Detector": run_ta030,
    "TA-045: Context Cleaner": run_ta045,
    "TA-048: Embedding Drift": run_ta048,
    "TA-050: Context Comparison": run_ta050,
    "TA-061: Reflection + Rewrite": run_ta061,
    "TA-065: Autonomy Logger": run_ta065,
    "TA-069: Agent Loop Map": run_ta069,
    "TA-084: Deployment Pinner": run_ta084,
    "TA-094: Feedback Rubric Scorer": run_ta094,
    "TA-100: Auto-Evolution Log": run_ta100
}

if selection in dashboard_map:
    dashboard_map[selection]()
