import os

from celery import Celery

redis_url = os.getenv("API_REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery("privacy_workers", broker=redis_url, backend=redis_url)
celery_app.autodiscover_tasks(["common", "discovery", "monitoring", "action"])
