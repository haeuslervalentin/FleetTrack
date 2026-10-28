from mcp.server.mcpserver import MCPServer

from mcp_server.tools.vehicles import register_vehicle_tools

mcp = MCPServer("FleetTrack")

register_vehicle_tools(mcp)

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
        json_response=True,
    )
