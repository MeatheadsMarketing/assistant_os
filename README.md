# 🧠 Assistant OS (TA Registry)

This is a modular, CLI + Raycast + Streamlit compatible operating system for managing intelligent assistants (Tiny Assistants or TAs) at scale.

---

## 📦 Key Components

| Folder | Purpose |
|--------|---------|
| `ta-registry/` | Modular assistant definitions (`TA-001` → `TA-100`) |
| `ta-registry/TA-###/config.json` | Instruction logic, domain, I/O, trigger |
| `ta-loader.sh` | CLI tool to list, run, or initialize assistants |
| `ta_registry_status.json` | Status tracker across build/deploy |
| `assistant_os_dashboard.py` | Streamlit dashboard for status, memory, health |
| `raycast_quicklinks.json` | Script launcher pack for Raycast integration |

---

## 🚀 Features

- 🔧 Modular CLI-based assistant logic (`ta-loader.sh`)
- ⚡ Raycast hotkey/launcher integration
- 📚 Streamlit UI with memory editor, status visualizer, health dashboards
- ✅ TA-099: Meta evaluator
- 🧠 TA-100: Auto-evolution engine
- 📊 10 Domains of intelligence: memory, validation, ops, toolchains, autonomy...

---

## 🧭 Streamlit App

Launch the full dashboard UI:

```bash
streamlit run assistant_os_dashboard.py
```

---

## 🔁 CLI Quickstart

```bash
cd ta-registry
./ta-loader.sh list        # List all assistants
./ta-loader.sh init TA-042 # Scaffold README + shell
./ta-loader.sh run TA-042  # Execute it
```

---

## 🧠 Full Catalog

See [`TA_REGISTRY_INDEX.md`](./TA_REGISTRY_INDEX.md) for all 100 assistants.

---

## 📂 Recommended Repo Structure

```
assistant-os-raycast/
├── assistant_os_dashboard.py
├── ta-loader.sh
├── ta-registry/
│   ├── TA-001/
│   │   ├── config.json
│   │   ├── ta001_instruction_diff.sh
│   │   └── README.md
│   ├── ...
│   └── ta_registry_status.json
├── ta_catalog.csv
├── TA_REGISTRY_INDEX.md
└── raycast_quicklinks.json
```

---

