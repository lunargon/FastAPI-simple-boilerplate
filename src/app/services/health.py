"""Example service for the health endpoint."""

from app.schemas.health import HealthResponse


def get_health() -> HealthResponse:
    return HealthResponse(status=200, msg="Ok")
