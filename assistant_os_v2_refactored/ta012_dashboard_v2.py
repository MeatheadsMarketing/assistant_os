import streamlit as st

def render_dashboard():
    def render_dashboard():

        import streamlit as st
        from pathlib import Path
        import json


        st.sidebar.title("🧠 TA Category: Memory Update")
        assistant = st.sidebar.radio("Choose Assistant", ["TA-012v2: Memory Injector"])

        fact_queue_path = Path("./ta-registry/TA-012/fact_queue.txt")
        memory_path = Path("./ta-registry/TA-012/memory.json")
        fact_queue_path.parent.mkdir(parents=True, exist_ok=True)
        memory_path.parent.mkdir(parents=True, exist_ok=True)

        if not memory_path.exists():
            memory_path.write_text(json.dumps({}, indent=2))
        if not fact_queue_path.exists():
            fact_queue_path.write_text("Preferred format: markdown list\nClient priority: responsiveness over cost")

        if assistant == "TA-012v2: Memory Injector":
            st.title("📥 TA-012 (v2): Memory Update with Approval")

            st.markdown("### 🧾 Current Fact Queue")
            facts = fact_queue_path.read_text().strip().split("\n")
            selected_facts = [f for f in facts if st.checkbox(f, value=True)]

            if st.button("✅ Inject Selected Facts"):
                memory = json.load(open(memory_path))
                for line in selected_facts:
                    if ":" in line:
                        key, value = line.split(":", 1)
                        memory[key.strip().replace(" ", "_").lower()] = value.strip()
                json.dump(memory, open(memory_path, "w"), indent=2)
                st.success("Memory updated with approved facts.")

            st.markdown("### 📂 Updated Memory Preview")
            st.json(json.load(open(memory_path)))