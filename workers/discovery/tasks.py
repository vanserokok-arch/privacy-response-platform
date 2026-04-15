from common.celery_app import celery_app


@celery_app.task(name="discovery.run_search_task")
def run_search_task(search_task_id: str) -> dict[str, str]:
    return {"search_task_id": search_task_id, "status": "queued_for_playwright_pipeline"}

