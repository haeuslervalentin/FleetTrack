from collections.abc import Callable

from mcp.server.mcpserver import MCPServer

from backend.services.list_vehicles import list_vehicles as get_vehicles_from_database


def register_vehicle_tools(mcp: MCPServer) -> None:
    @mcp.tool()
    def list_vehicles() -> list[dict]:
        """
        Returns every vehicle in the database as a list.
        """

        return get_vehicles_from_database()
