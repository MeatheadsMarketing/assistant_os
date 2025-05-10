import streamlit as st

def render_dashboard():
    def render_dashboard():

        import streamlit as st
        from pathlib import Path


        st.sidebar.title("🧠 TA Category: Memory Extractor")
        assistant = st.sidebar.radio("Choose Assistant", ["TA-013v2: Fact Extractor"])

        output_path = Path("./ta-registry/TA-013/last_output.txt")
        queue_path = Path("./ta-registry/TA-012/fact_queue.txt")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        queue_path.parent.mkdir(parents=True, exist_ok=True)

        if not output_path.exists():
            output_path.write_text("Client prefers markdown.
        Project status: delayed.
        Key risk: lack of clarity.")

        if assistant == "TA-013v2: Fact Extractor":
            st.title("🧠 TA-013 (v2): Extract from Assistant Output")

            st.markdown("### 📄 Parsed Output")
            lines = output_path.read_text().strip().split("\n")
            approved = [line for line in lines if st.checkbox(line, value=True)]

            if st.button("📌 Queue Selected Facts"):
                with open(queue_path, "a") as f:
                    for line in approved:
                        f.write(line + "\n")
                st.success("Facts queued for TA-012 injection.")