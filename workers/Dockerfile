FROM python:3.12-slim

WORKDIR /worker
COPY workers /worker
RUN pip install --no-cache-dir -e .

CMD ["celery", "-A", "common.celery_app.celery_app", "worker", "--loglevel=info"]
