# Privacy Response Platform

Production-oriented monorepo scaffold for a privacy/legal-tech platform focused on Russia/CIS first, with architecture ready for international expansion.

## Why this product exists

Most consumer privacy products focus on broker opt-outs. This platform is designed for higher-stakes response operations:

- digital footprint discovery across open web/search/social traces,
- identity resolution with confidence and evidence,
- source clustering (including mirrors/republish patterns),
- risk scoring and remediation prioritization,
- multi-path action orchestration (site, host, index, legal),
- legal workflow support with auditable evidence,
- continuous monitoring and reappearance defense.

## Core modules in this scaffold

1. Identity Engine  
2. Discovery Engine  
3. Source Graph  
4. Risk Engine  
5. Action Orchestrator  
6. Legal Engine  
7. Monitoring Engine  
8. Evidence Vault

## Monorepo structure

```text
apps/
  api/      # FastAPI + SQLAlchemy + Alembic backend
  web/      # Next.js App Router operator console
workers/    # Celery workers for discovery/monitoring/actions
packages/
  shared/   # shared primitives for Python/TypeScript
docs/       # product, architecture, roadmap
```

## Current implementation snapshot

Implemented:
- API app entrypoint, config, health endpoint, DB session.
- SQLAlchemy models for all initial domain entities.
- Alembic baseline migration.
- CRUD skeleton for cases and identifiers + source list endpoint.
- Worker task modules (discovery, monitoring, action).
- Next.js operations shell with dashboard/cases/sources/monitoring/legal pages.
- Docker + docker-compose + `.env.example` + Makefile.

Not implemented yet:
- advanced identity resolution scoring logic,
- real discovery connectors/parsers,
- legal template generation, evidence capture pipeline,
- authN/authZ, tenancy, RBAC,
- full test suite and CI quality gates.

## Local development

1. Copy environment:

```bash
cp .env.example .env
```

2. Start stack:

```bash
make up
```

> `docker-compose` now consumes `.env` (not `.env.example`) and applies Alembic migrations on API container startup.

3. API docs:
- http://localhost:8000/docs

4. Web console:
- http://localhost:3000

## API endpoints scaffolded

- `GET /health`
- `POST /cases`
- `GET /cases`
- `GET /cases/{case_id}`
- `POST /cases/{case_id}/identifiers`
- `GET /cases/{case_id}/sources`

## Runtime verification (docker-compose end-to-end)

1. Ensure env exists:

```bash
cp .env.example .env
```

2. Start all services:

```bash
docker compose up --build -d
```

3. Check API health (includes Postgres + Redis connectivity):

```bash
curl -sS http://localhost:8000/health
```

4. Verify frontend is up and rendering dashboard:

```bash
curl -I http://localhost:3000
```

5. Verify Celery task execution:

```bash
docker compose exec worker celery -A common.celery_app.celery_app call common.ping --args='["runtime-check"]'
```

6. Verify S3/MinIO upload path:

```bash
docker compose exec api python scripts/s3_smoke_test.py
```
