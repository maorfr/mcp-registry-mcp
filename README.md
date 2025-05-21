# mcp-registry-mcp

MCP server for mcp-registry: https://github.com/modelcontextprotocol/registry

## Available MCP Tools

This MCP server exposes the following tools:

### 1. list_registry_server_entries
**Description:** Lists MCP registry server entries with pagination support.
**Parameters:** None

---

### 2. get_server_details
**Description:** Get details for a specific MCP registry server.
**Parameters:**
- `server_id` (str): The ID of the server to retrieve details for.

---

### 3. publish_server_entry
**Description:** Publishes a new MCP server entry to the registry. Authentication is required via Bearer token in the Authorization header.
**Parameters:**
- `server_name` (str): The name of the server to publish.
- `description` (str): A description for the server.

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
        "-e", "MCP_REGISTRY_API_KEY",
        "quay.io/maorfr/mcp-registry-mcp"
      ],
      "env": {
        "MCP_REGISTRY_URL": "https://your-domain.mcp-registry.co",
        "MCP_REGISTRY_API_KEY": "REDACTED",
      }
    }
  }
}
```
