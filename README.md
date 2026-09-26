# MCP Learning Log

A small MCP (Model Context Protocol) server that lets Claude log, search, and
summarize things you learn during a conversation, and push them to GitHub as
a formatted markdown doc.

## What this project implements

- Two tools: `add_learning`, `search_learnings`
- One resource: `learnings://all` (raw JSON of every entry)
- One prompt: `summarize_week`
- One tool to push the log to a GitHub repo: `push_to_github`
- A Claude Desktop config to connect the server locally

## File structure

- `server.py` — the MCP server: tools, resource, prompt
- `pyproject.toml` — project deps (managed by uv)
- `uv.lock` — locked dependency versions
- `.python-version` — pinned Python version
- `.gitignore`
- `.env.example` — template for GitHub token/repo config
- `config/claude_desktop_config.json` — example Claude Desktop connection config

## Branches

| Branch | Adds |
|---|---|
| `step-0-setup` | project scaffold, no server code yet |
| `step-1-first-tool` | `add_learning` tool |
| `step-2-second-tool` | `search_learnings` tool |
| `step-3-resource` | `learnings://all` resource |
| `step-4-prompt` | `summarize_week` prompt |
| `step-5-claude-desktop` | Claude Desktop connection config |
| `step-6-github-push` | `push_to_github` tool |

Checkout any branch to see the project at that exact stage:
```bash
git checkout step-3-resource
```

## Setup

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv sync
```

Run the server with the MCP Inspector:
```bash
uv run mcp dev server.py
```