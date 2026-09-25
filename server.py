import json
import os
from datetime import datetime
from typing import Annotated

from pydantic import Field
from mcp.server import MCPServer

mcp = MCPServer("learning-log")
DATA_FILE = os.path.join(os.path.dirname(__file__), "learnings.json")


def _load():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def _save(entries):
    with open(DATA_FILE, "w") as f:
        json.dump(entries, f, indent=2)


@mcp.tool()
def add_learning(
    topic: Annotated[str, Field(description="Short title for the entry, e.g. 'MCP tools vs resources'")],
    details: Annotated[str, Field(description="A thorough, multi-sentence explanation of what was learned, written so someone with no context could understand the concept just from reading this")],
) -> str:
    """Save a new learning entry. Call this whenever the user shares something
    they learned during the conversation, even multiple times across a long chat.
    Write 'details' as a real, thorough explanation, several sentences covering
    what the concept is, how it works, and why it matters, not a short tag or summary."""
    entries = _load()
    entries.append({
        "topic": topic,
        "details": details,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    _save(entries)
    return f"Saved: {topic}"


@mcp.tool()
def search_learnings(
    keyword: Annotated[str, Field(description="Word to search for in saved topics or details")],
) -> str:
    """Search saved learnings for a keyword in the topic or details."""
    entries = _load()
    matches = [
        e for e in entries
        if keyword.lower() in e["topic"].lower() or keyword.lower() in e["details"].lower()
    ]
    if not matches:
        return f"No learnings found for '{keyword}'"
    return "\n\n".join(f"[{e['date']}] {e['topic']}\n{e['details']}" for e in matches)


if __name__ == "__main__":
    mcp.run()