from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.dependencies.services import get_case_service, get_identifier_service, get_source_repository
from app.repositories.source_repository import SourceRepository
from app.schemas.case import CaseCreate, CaseRead
from app.schemas.identifier import IdentifierCreate, IdentifierRead
from app.schemas.source import SourceRecordRead
from app.services.case_service import CaseService
from app.services.identifier_service import IdentifierService

router = APIRouter(prefix="/cases", tags=["cases"])


@router.post("", response_model=CaseRead, status_code=status.HTTP_201_CREATED)
def create_case(payload: CaseCreate, service: CaseService = Depends(get_case_service)) -> CaseRead:
    return service.create(payload)


@router.get("", response_model=list[CaseRead])
def list_cases(service: CaseService = Depends(get_case_service)) -> list[CaseRead]:
    return service.list()


@router.get("/{case_id}", response_model=CaseRead)
def get_case(case_id: UUID, service: CaseService = Depends(get_case_service)) -> CaseRead:
    return service.get(case_id)


@router.post("/{case_id}/identifiers", response_model=IdentifierRead, status_code=status.HTTP_201_CREATED)
def create_case_identifier(
    case_id: UUID,
    payload: IdentifierCreate,
    service: IdentifierService = Depends(get_identifier_service),
) -> IdentifierRead:
    return service.create_for_case(case_id, payload)


@router.get("/{case_id}/sources", response_model=list[SourceRecordRead])
def list_case_sources(
    case_id: UUID, repo: SourceRepository = Depends(get_source_repository)
) -> list[SourceRecordRead]:
    rows = repo.list_for_case(case_id)
    return [
        SourceRecordRead(
            source_record_id=source.id,
            domain=source.domain,
            url=source.url,
            source_type=source.source_type,
            match_score=match.match_score,
        )
        for match, source in rows
    ]
