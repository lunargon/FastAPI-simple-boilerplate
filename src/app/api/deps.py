"""Shared API dependencies (DB sessions, auth, pagination, ...)."""

from app.db.session import get_mongo_db, get_sql_db

__all__ = ["get_mongo_db", "get_sql_db"]
