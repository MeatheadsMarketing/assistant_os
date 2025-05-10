import streamlit as st
from cover_page import render_cover_page
from status_dashboard_tab import render_status_dashboard
from memory_editor_tab import render_memory_editor
from ta_browser_tab import render_ta_browser
from ta_health_tab import render_ta_health_tab
from phase_launcher_tab import render_phase_launcher_tab
from utilities_tab import render_utilities_tab

tab = st.sidebar.radio("📂 Command Deck Tabs", [
    "📘 Cover Page",
    "📊 Status Dashboard",
    "🧠 Memory Editor",
    "🔍 TA Browser",
    "🧬 TA Health",
    "🚀 Phase Launcher",
    "🛠️ Utilities Panel"
])

if tab == "📘 Cover Page":
    render_cover_page()
elif tab == "📊 Status Dashboard":
    render_status_dashboard()
elif tab == "🧠 Memory Editor":
    render_memory_editor()
elif tab == "🔍 TA Browser":
    render_ta_browser()
elif tab == "🧬 TA Health":
    render_ta_health_tab()
elif tab == "🚀 Phase Launcher":
    render_phase_launcher_tab()
elif tab == "🛠️ Utilities Panel":
    render_utilities_tab()