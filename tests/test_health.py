"""Health endpoint tests."""

from fastapi import status
from fastapi.testclient import TestClient


def test_healthcheck(client: TestClient) -> None:
    res = client.get("/healthcheck/")
    assert res.status_code == status.HTTP_200_OK
    assert res.json() == {"status": 200, "msg": "Ok"}


def test_healthcheck_versioned(client: TestClient) -> None:
    res = client.get("/api/v1/healthcheck/")
    assert res.status_code == status.HTTP_200_OK
    assert res.json() == {"status": 200, "msg": "Ok"}
