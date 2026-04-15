PYTHON ?= python3

.PHONY: bootstrap up down api-lint api-test web-lint format migrate runtime-health runtime-celery runtime-s3

bootstrap:
	test -f .env || cp .env.example .env
	cd apps/api && $(PYTHON) -m venv .venv && . .venv/bin/activate && pip install -e .[dev]
	cd apps/web && npm install

up:
	docker compose up --build

down:
	docker compose down -v

api-lint:
	cd apps/api && . .venv/bin/activate && ruff check app

api-test:
	cd apps/api && . .venv/bin/activate && pytest

migrate:
	cd apps/api && . .venv/bin/activate && alembic upgrade head

runtime-health:
	curl -fsS http://localhost:8000/health

runtime-celery:
	docker compose exec worker celery -A common.celery_app.celery_app call common.ping --args='[\"runtime-check\"]'

runtime-s3:
	docker compose exec api python scripts/s3_smoke_test.py

web-lint:
	cd apps/web && npm run lint

format:
	cd apps/api && . .venv/bin/activate && ruff format app
	cd apps/web && npm run format
