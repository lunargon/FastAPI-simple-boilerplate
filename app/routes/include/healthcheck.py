from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/")
async def healthcheck():
    """healthcheck api"""
    return {
        "status": 200,
        "msg": "Ok"
    }
