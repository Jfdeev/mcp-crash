from typing import List

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return "It always rains in Seattle."

if __name__ == "__main__":
    mcp.run(transport="sse")