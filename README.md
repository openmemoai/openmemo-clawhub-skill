# OpenMemo — Persistent Memory for OpenClaw Agents

> Stop agents from repeating tasks. Give your AI long-term memory.

A ClawHub Skill that connects OpenClaw agents to [OpenMemo](https://github.com/openmemoai/openmemo), the open-source Memory Infrastructure for AI Agents.

## Features

- **Persistent agent memory** — memories survive across sessions
- **Task deduplication** — agents check before re-executing completed work
- **Scene-aware recall** — context-specific memory retrieval (coding, debug, research)
- **Memory inspector** — built-in dashboard to monitor memory behavior
- **Local-first** — your data stays on your machine

## Architecture

```
User
 │
 ▼
OpenClaw Agent
 │
 ▼
OpenMemo Skill (ClawHub)
 │
 ├─ Bootstrap Mode        (adapter not detected)
 │     → installation guide
 │     → setup wizard
 │
 └─ Memory Mode           (adapter detected)
       → recall_memory
       → write_memory
       → check_task_memory
       │
       ▼
 OpenMemo Adapter (local)
       │
       ▼
 OpenMemo Memory Engine
```

## Quick Start

### 1. Install this skill on ClawHub

### 2. Install the adapter locally

```bash
pip install openmemo openmemo-openclaw
```

### 3. Start the memory server

```bash
openmemo serve
```

### 4. Restart your agent

The skill automatically detects the running adapter and enters Memory Mode.

## Tools

| Tool | Description |
|------|-------------|
| `recall_memory` | Retrieve relevant past experience |
| `write_memory` | Store structured memory events |
| `check_task_memory` | Check if a task was already completed |

## Memory Rules

The skill injects operating rules into the agent's prompt:

1. **Before any task** → call `check_task_memory` to avoid duplication
2. **Before decisions** → call `recall_memory` for past experience
3. **After important tasks** → call `write_memory` to save experience

## Python Usage

```python
from openmemo_clawhub_skill import OpenMemoSkill

skill = OpenMemoSkill()
result = skill.run()

if result["mode"] == "memory":
    # Memory tools are available
    recall = skill.recall("database optimization patterns")
    skill.write("PostgreSQL: use EXPLAIN ANALYZE before optimizing", scene="coding")
    check = skill.check_task("deploy staging environment")
else:
    # Show setup instructions
    print(result["message"])
```

## Configuration

| Env Variable | Default | Description |
|---|---|---|
| `OPENMEMO_ENDPOINT` | `http://localhost:8765` | OpenMemo adapter endpoint |

## Security

- **Localhost only** — adapter binds to 127.0.0.1 by default
- **No cloud** — all memory stays local unless you configure cloud sync
- **No telemetry** — zero data collection

## License

Apache-2.0
