# Architecture Overview

## System layers

1. **Presentation Layer** (`apps/web`)  
   Operator console for case management, source operations, legal workflow, monitoring.
2. **API Layer** (`apps/api`)  
   FastAPI service exposing domain-oriented endpoints.
3. **Domain/Data Layer** (`apps/api/app/models`, `repositories`, `services`)  
   Case-centric entities and service boundaries.
4. **Async Execution Layer** (`workers`)  
   Celery workers for heavy discovery, recurring monitoring, and action dispatch.
5. **Shared Contracts Layer** (`packages/shared`)  
   Cross-service enums/constants and module identifiers.
6. **Infra Layer** (`docker-compose`, env, Makefile)  
   Local production-like bootstrap baseline.

## Module boundaries

- **Identity Engine**: `person_profiles`, `identifiers`, resolution service (future).
- **Discovery Engine**: `search_tasks`, discovery workers, Playwright connectors (future).
- **Source Graph**: `source_records`, `source_matches`, cluster keys.
- **Risk Engine**: `risk_assessments`, scoring policies (future).
- **Action Orchestrator**: `removal_actions`, provider/adaptor orchestration (future).
- **Legal Engine**: `legal_documents`, jurisdiction templates (future).
- **Monitoring Engine**: `monitor_rules`, `alerts`, recurring worker tasks.
- **Evidence Vault**: `evidence_snapshots`, S3 abstraction for immutable records.

## Data flow (initial)

1. API receives case + identifier inputs.
2. Discovery workers execute search tasks and generate source records/matches.
3. Risk engine computes case risk posture from match graph.
4. Orchestrator emits removal/legal actions.
5. Evidence snapshots and legal documents persisted to storage.
6. Monitoring worker rechecks exposures and emits alerts.

## Async jobs

- `discovery.run_search_task`
- `monitoring.run_monitor_cycle`
- `action.execute_removal`

## Evidence and legal strategy

- Evidence writes use S3-compatible abstraction (MinIO/AWS S3-ready).
- Every material action should attach evidence references and timestamps.
- Legal documents are first-class entities, enabling auditable workflows across jurisdictions.

