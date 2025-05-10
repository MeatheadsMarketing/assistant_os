import streamlit as st

def render_dashboard():
    def render_dashboard():

        import streamlit as st
        import graphviz


        st.sidebar.title("🔁 TA Category: Agent Feedback")
        assistant = st.sidebar.radio("Choose Assistant", ["TA-069v2: Multi-Agent Loop Map"])

        if assistant == "TA-069v2: Multi-Agent Loop Map":
            st.title("🔁 TA-069 (v2): Visual Agent Loop Trace")

            st.markdown("Simulate agent-to-agent loop progression.")

            agent_chain = st.text_area("Comma-separated Agents in Feedback Loop", value="SummarizerGPT, PlannerGPT, ValidatorGPT")

            if st.button("📊 Render Loop Trace"):
                agents = [a.strip() for a in agent_chain.split(",")]
                dot = graphviz.Digraph()
                for i, agent in enumerate(agents):
                    dot.node(agent)
                    if i > 0:
                        dot.edge(agents[i-1], agent)
                dot.edge(agents[-1], agents[0])  # Loop closure
                st.graphviz_chart(dot)