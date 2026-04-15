from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from redis import Redis
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import SessionLocal

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> JSONResponse:
    db_status = "ok"
    redis_status = "ok"

    db: Session = SessionLocal()
    try:
        db.execute(text("SELECT 1"))
    except SQLAlchemyError:
        db_status = "error"
    finally:
        db.close()

    try:
        redis_client = Redis.from_url(settings.redis_url, decode_responses=True)
        redis_client.ping()
    except Exception:
        redis_status = "error"

    overall = "ok" if db_status == "ok" and redis_status == "ok" else "degraded"
    payload = {"status": overall, "database": db_status, "redis": redis_status}
    code = status.HTTP_200_OK if overall == "ok" else status.HTTP_503_SERVICE_UNAVAILABLE
    return JSONResponse(status_code=code, content=payload)
