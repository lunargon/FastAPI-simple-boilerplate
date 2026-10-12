"""Shared pytest fixtures."""

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# Ensure `src/` layout is importable without installing the package.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from app.main import app  # noqa: E402


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(app)
