# mcp-registry-mcp

MCP server for mcp-registry: https://github.com/modelcontextprotocol/registry

## Available MCP Tools

This MCP server exposes the following tools:

### 1. health_check
**Description:** Checks the health of the MCP registry server.
**Parameters:** None

---

### 2. list_registry_server_entries
**Description:** Lists MCP registry server entries with pagination support.
**Parameters:** None

---

### 3. get_server_details
**Description:** Get details for a specific MCP registry server.
**Parameters:**
- `server_id` (str): The ID of the server to retrieve details for.

---

### 4. ping
**Description:** Simple ping endpoint that returns environment configuration information.
**Parameters:** None

---

## Running with Podman or Docker

You can run the mcp-registry-mcp server in a container using Podman or Docker:

Example configuration for running with Podman:

```json
{
  "mcpServers": {
    "mcp-registry": {
      "command": "podman",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "MCP_REGISTRY_URL",
        "-e", "MCP_TRANSPORT"
        "quay.io/maorfr/mcp-registry-mcp:latest"
      ],
      "env": {
        "MCP_REGISTRY_URL": "https://your-domain.mcp-registry.co",
        "MCP_TRANSPORT": "sse"
      }
    }
  }
}
```
