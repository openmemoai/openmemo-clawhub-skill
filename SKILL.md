# OpenMemo Memory

Persistent memory system for OpenClaw agents.

## Description

OpenMemo adds persistent memory to OpenClaw agents. Instead of relying only on chat history or large memory files, OpenMemo allows agents to remember tasks, decisions, and workflows.

Your agent can:
- Remember completed tasks
- Reuse successful workflows
- Avoid duplicate execution
- Accumulate long-term operational knowledge

## Tools

### recall_memory

Retrieve relevant memory from OpenMemo. Use this to recall past experience, decisions, and knowledge before executing tasks.

**Parameters:**
- `query` (string, required): The search query for memory recall
- `scene` (string, optional): Scene context (e.g., coding, debug, research, deployment)

### write_memory

Store structured memory event in OpenMemo. Use this after completing important tasks to save experience for future use.

**Parameters:**
- `content` (string, required): The memory content to store
- `scene` (string, optional): Scene context
- `type` (string, optional): Memory type — fact, decision, observation, preference

### check_task_memory

Check if a task has already been executed. Use this FIRST before starting any task to avoid duplication.

**Parameters:**
- `task_description` (string, required): Description of the task to check

## Rules

When executing tasks, follow these memory operating rules:

1. BEFORE starting any task, call `check_task_memory` with the task description. If a successful previous execution exists, reuse the result or skip.

2. Use `recall_memory` to retrieve relevant past experience before making decisions.

3. After completing important tasks, call `write_memory` to store structured experience: decisions made, successful approaches, errors resolved, key observations.

4. Always include the scene context (coding, debug, research, deployment) for better recall accuracy.

## Setup

Install the OpenMemo adapter locally:

```
pip install openmemo openmemo-openclaw
openmemo serve
```

Restart your agent. The Skill will automatically detect the adapter and activate persistent memory.

## Features

- Persistent agent memory across sessions
- Task deduplication — stop repeating work
- Scene-aware recall (coding, debug, research, deployment)
- Memory inspector dashboard
- Local-first architecture — your data stays local

## Links

- GitHub: https://github.com/openmemoai/openmemo
- Adapter: https://github.com/openmemoai/openmemo-openclaw-adapter
