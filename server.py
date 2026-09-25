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
    topic: Annotated[str, Field(description="What the entry is about, e.g. 'MCP tools'")],
    note: Annotated[str, Field(description="What was learned about this topic")],
) -> str:
    """Save a new learning entry with a topic and a note."""
    entries = _load()
    entries.append({
        "topic": topic,
        "note": note,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    _save(entries)
    return f"Saved: {topic}"


if __name__ == "__main__":
    mcp.run()