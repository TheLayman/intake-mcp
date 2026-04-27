"""MCP server entry point.

This is a minimal stub. You're expected to:
- Register MCP tools that wrap the patient-intake API.
- Validate inputs.
- Surface errors in a way that's useful to an agent calling these tools.

Feel free to restructure entirely — this is just a starting point.
"""
from __future__ import annotations

from mcp.server import Server
from mcp.server.stdio import stdio_server

from .client import IntakeAPIClient

server = Server("intake-mcp")
_client = IntakeAPIClient()


# TODO: register tools using @server.list_tools / @server.call_tool decorators
# (or whatever pattern the MCP SDK provides). Required at minimum:
#   - get_patient(patient_id: str) -> Patient
#   - create_patient(...) -> Patient
#   - list_patients(...) -> list[Patient]
#   - create_appointment(...) -> Appointment
#   - list_appointments_for_patient(patient_id: str, ...) -> list[Appointment]


def main() -> None:
    import asyncio

    async def run() -> None:
        async with stdio_server() as (read_stream, write_stream):
            await server.run(read_stream, write_stream, server.create_initialization_options())

    asyncio.run(run())


if __name__ == "__main__":
    main()
