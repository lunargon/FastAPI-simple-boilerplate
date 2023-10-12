from fastapi import APIRouter

from app.routes.include import healthcheck

api_router = APIRouter()
api_router.include_router(healthcheck.router, prefix="/healthcheck", tags=["healthcheck"])

# api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
# api_router.include_router(users.router, prefix="/users", tags=["users"])