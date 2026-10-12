"""v1 router: include all v1 endpoint modules here."""

from fastapi import APIRouter

from app.api.v1.health import router as health_router

router = APIRouter()
router.include_router(health_router, prefix="/healthcheck", tags=["healthcheck"])

# router.include_router(auth.router, prefix="/auth", tags=["auth"])
# router.include_router(users.router, prefix="/users", tags=["users"])
