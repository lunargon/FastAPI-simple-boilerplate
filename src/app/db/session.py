"""Database helpers: lazy SQL engine/session + Mongo client.

Nothing connects at import time so `import app.main` never needs a live DB.
"""

import logging
from collections.abc import Generator, Iterator
from functools import lru_cache
from typing import Any

from pymongo import MongoClient
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings

log = logging.getLogger(__name__)


@lru_cache
def get_sql_engine() -> Engine:
    if not settings.SQL_DATABASE_URL:
        raise RuntimeError("SQL_DATABASE_URL is not set")
    kwargs: dict[str, Any] = {"pool_pre_ping": True}
    if settings.SQL_DATABASE_URL.startswith("sqlite"):
        kwargs["connect_args"] = {"check_same_thread": False}
    return create_engine(settings.SQL_DATABASE_URL, **kwargs)


@lru_cache
def get_sql_session_factory() -> sessionmaker[Session]:
    return sessionmaker(autocommit=False, autoflush=False, bind=get_sql_engine())


def get_sql_db() -> Iterator[Session]:
    """FastAPI dependency yielding a SQL session."""
    db = get_sql_session_factory()()
    try:
        yield db
    finally:
        db.close()


@lru_cache
def get_mongo_client() -> MongoClient[Any]:
    if not settings.MONGO_DATABASE_URL:
        raise RuntimeError("MONGO_DATABASE_URL is not set")
    log.info("Creating MongoDB client")
    return MongoClient(settings.MONGO_DATABASE_URL)


def get_mongo_db() -> Generator[Any, None, None]:
    """FastAPI dependency yielding the default Mongo database."""
    client = get_mongo_client()
    yield client.get_default_database()
