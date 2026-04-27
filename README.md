# intake-mcp

A skeleton for an MCP server that wraps a patient-intake REST API.

## What's here

```
intake-mcp/
├── pyproject.toml
├── README.md
├── .gitignore
├── src/intake_mcp/
│   ├── __init__.py
│   ├── server.py                ← MCP server entry point (stub)
│   └── client.py                ← HTTP client wrapper (stub)
└── tests/
    └── __init__.py
```

The shape of `server.py` and `client.py` is intentionally minimal — you decide the structure.

## Setup

```bash
pip install -e ".[dev]"
```

## Target API

The target is a small FastAPI service exposing patient and appointment endpoints with bearer auth. It's provided alongside this skeleton.

```bash
docker run -p 8000:8000 -e API_TOKEN=intake-demo-token intake-api
```

Set `CHAOS=1` on the API container to enable transient 503s on ~15% of requests.

## What to build

At minimum:

- An MCP server (`server.py`) exposing tools that wrap the patient-intake API.
- An HTTP client (`client.py`) handling auth, retries, and error normalization.
- At least one **integration test** that runs against the actual API.

Required tools at minimum:

- `get_patient(patient_id)`
- `create_patient(...)`
- `list_patients(...)`
- `create_appointment(...)`
- `list_appointments_for_patient(patient_id, ...)`

You may add more tools if useful. You may rename them if your reasoning is sound.

## Running tests

```bash
# Start the target API in another terminal first, then:
pytest
```
