from common.celery_app import celery_app


@celery_app.task(name="action.execute_removal")
def execute_removal(action_id: str) -> dict[str, str]:
    return {"action_id": action_id, "status": "submitted"}

