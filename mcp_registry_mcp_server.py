import os
from enum import Enum
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-registry")

MCP_REGISTRY_API_BASE = f"{os.environ['MCP_REGISTRY_URL']}/v0"


async def make_request(
    url: str, method: str = "GET", data: dict[str, Any] = None
) -> dict[str, Any] | None:
    api_key = os.environ.get("MCP_REGISTRY_API_KEY")
    if api_key:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        }
    else:
        headers = {}

    async with httpx.AsyncClient() as client:
        if method.upper() == "GET":
            response = await client.request(method, url, headers=headers, params=data)
        else:
            response = await client.request(method, url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def health_check():
    """Checks the health of the MCP registry server."""
    url = f"{MCP_REGISTRY_API_BASE}/health"
    response = await make_request(url)
    return response


def format_servers(data: list[dict[str, Any]]) -> str:
    lines = []
    for item in data:
        lines.append(f"MCP Server Name: {item['name']}")
        lines.append(f"MCP Server ID: {item['id']}")
    return "\n".join(lines)


@mcp.tool()
async def list_registry_server_entries():
    """Lists MCP registry server entries with pagination support."""
    url = f"{MCP_REGISTRY_API_BASE}/servers"
    response = await make_request(url)
    return format_servers(response["servers"])


@mcp.tool()
async def get_server_details(server_id: str):
    """Get details for a specific MCP registry server."""
    url = f"{MCP_REGISTRY_API_BASE}/servers/{server_id}"
    response = await make_request(url)
    return format_servers([response])


@mcp.tool()
async def ping():
    """Simple ping endpoint that returns environment configuration information."""
    url = f"{MCP_REGISTRY_API_BASE}/ping"
    response = await make_request(url)
    return response


if __name__ == "__main__":
    mcp.run(transport=os.environ.get("MCP_TRANSPORT", "stdio"))
