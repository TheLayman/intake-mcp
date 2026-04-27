"""HTTP client wrapper for the patient-intake API.

This is a minimal stub. You're expected to fill in:
- Auth (Bearer token)
- Retry policy (the API returns 503 under chaos mode)
- Error normalization (how do you surface 4xx vs 5xx vs network errors?)
- Type hints / response shapes

Feel free to restructure this file completely — the shape here is just a hint.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

import httpx


@dataclass
class IntakeAPIConfig:
    base_url: str = os.getenv("INTAKE_API_URL", "http://localhost:8000")
    api_token: str = os.getenv("INTAKE_API_TOKEN", "intake-demo-token")
    timeout_seconds: int = 10


class IntakeAPIClient:
    def __init__(self, config: Optional[IntakeAPIConfig] = None):
        self.config = config or IntakeAPIConfig()
        # TODO: configure httpx.Client with auth header, timeout, etc.
        self._http = httpx.Client(base_url=self.config.base_url)

    def get_patient(self, patient_id: str) -> dict:
        # TODO: implement, including auth, retry, error handling
        raise NotImplementedError

    # TODO: add the rest of the methods needed by your MCP tools
