from mcp.server.fastmcp import FastMCP

mcp = FastMCP('Chess.com')

from .chess_api import (
    get_player_profile,
    get_player_stats,
    get_player_is_online,
    get_player_current_games,
)


@mcp.tool()
def get_chess_player_profile(username: str):
    """Get the public profile for a Chess.com player by username."""
    return get_player_profile(username)


@mcp.tool()
def get_chess_player_stats(username: str):
    """Get the stats for a Chess.com player by username."""
    return get_player_stats(username)


@mcp.tool()
def get_chess_player_is_online(username: str):
    """Check whether a Chess.com player is currently online."""
    return get_player_is_online(username)


@mcp.tool()
def get_chess_player_current_games(username: str):
    """Get the list of current games (live and daily) for a Chess.com player by username."""
    return get_player_current_games(username)

