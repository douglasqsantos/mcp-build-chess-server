# mcp-build-chess-server

A minimal [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that exposes **Chess.com** player profile and stats as tools. It runs over **stdio** so MCP clients (e.g. Cursor, Claude Desktop) can run it as a subprocess. The project uses **uv** for dependency management; you can run it locally with `uv run chess-server` or via **uvx** from Git.

## Project structure

```bash
mcp-build-chess-server/
├── src/chess/
│   ├── __init__.py
│   ├── __main__.py      # Entry point (chess-server)
│   ├── server.py        # FastMCP app and tools
│   └── chess_api.py     # Chess.com API client
├── pyproject.toml       # Project and [project.scripts] chess-server
├── uv.lock
└── README.md
```

## Prerequisites

- **Python 3.12+**
- **[uv](https://docs.astral.sh/uv/)** (recommended) or pip

## How to run

### Option 1: Local (uv)

From the project directory:

```bash
uv sync
uv run chess-server
```

The server uses **stdio**; an MCP client (Cursor, Claude Desktop, etc.) typically starts it as a subprocess and talks over stdin/stdout.

### Option 2: Run with uvx (from Git)

Install and run from the repository without cloning (requires [uv](https://docs.astral.sh/uv/)):

```bash
uvx --from git+https://github.com/douglasqsantos/mcp-build-chess-server.git chess-server
```

Replace with your repo URL. The server runs with the same behavior (stdio transport).

## Connecting a client

### Cursor

Add to your MCP config (e.g. `~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "Chess.com": {
      "command": "/opt/homebrew/bin/uv",
      "args": [
        "--directory",
        "/path/to/mcp-build-chess-server",
        "run",
        "--frozen",
        "chess-server"
      ]
    }
  }
}
```

Or with **uvx** from Git:

```json
{
  "mcpServers": {
    "Chess.com": {
      "command": "/opt/homebrew/bin/uvx",
      "args": [
        "--from",
        "git+https://github.com/douglasqsantos/mcp-build-chess-server.git",
        "chess-server"
      ]
    }
  }
}
```

Restart Cursor (or reload MCP) so the **Chess.com** server is available.

### Claude Desktop

Add a server entry that runs the script via uv (stdio):

```json
{
  "mcpServers": {
    "Chess.com": {
      "command": "/opt/homebrew/bin/uv",
      "args": [
        "--directory",
        "/path/to/mcp-build-chess-server",
        "run",
        "chess-server"
      ]
    }
  }
}
```

Or with **uvx** from Git:

```json
{
  "mcpServers": {
    "Chess.com": {
      "command": "/opt/homebrew/bin/uvx",
      "args": [
        "--from",
        "git+https://github.com/douglasqsantos/mcp-build-chess-server.git",
        "chess-server"
      ]
    }
  }
}
```

Restart Claude Desktop and use the tools in chat (e.g. “Get the Chess.com profile for user X”).

## Tools

- **`get_chess_player_profile(username)`** — Get the public profile for a Chess.com player by username.
- **`get_chess_player_stats(username)`** — Get the stats for a Chess.com player by username.
- **`get_chess_player_is_online(username)`** — Check whether a Chess.com player is currently online.
- **`get_chess_player_current_games(username)`** — Get the list of current games (live and daily) for a Chess.com player by username.

## License

MIT License. See [LICENSE](LICENSE) for details.
