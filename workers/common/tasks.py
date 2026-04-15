from common.celery_app import celery_app


@celery_app.task(name="common.ping")
def ping(payload: str = "pong") -> dict[str, str]:
    return {"status": "ok", "payload": payload}

