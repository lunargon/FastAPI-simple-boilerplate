"""Health response schema."""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: int = 200
    msg: str = "Ok"
