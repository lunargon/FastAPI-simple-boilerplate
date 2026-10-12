"""Top-level API router (mount versioned routers here)."""

from fastapi import APIRouter

from app.api.v1.router import router as v1_router

api_router = APIRouter()
api_router.include_router(v1_router, prefix="/api/v1")

# Backwards-compatible alias (old code imported `api_router` from routes):
router = api_router
