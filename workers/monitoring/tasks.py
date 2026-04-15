from common.celery_app import celery_app


@celery_app.task(name="monitoring.run_monitor_cycle")
def run_monitor_cycle(case_id: str) -> dict[str, str]:
    return {"case_id": case_id, "status": "scheduled_monitoring_scan"}

