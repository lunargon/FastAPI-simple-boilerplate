"""Healthcheck endpoint."""

from fastapi import APIRouter

from app.schemas.health import HealthResponse
from app.services.health import get_health

router = APIRouter()


@router.get("/", response_model=HealthResponse)
async def healthcheck() -> HealthResponse:
    """Liveness probe."""
    return get_health()
