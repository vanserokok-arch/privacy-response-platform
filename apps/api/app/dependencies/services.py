from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.case_repository import CaseRepository
from app.repositories.identifier_repository import IdentifierRepository
from app.repositories.source_repository import SourceRepository
from app.services.case_service import CaseService
from app.services.identifier_service import IdentifierService


def get_case_service(db: Session = Depends(get_db)) -> CaseService:
    return CaseService(CaseRepository(db))


def get_identifier_service(db: Session = Depends(get_db)) -> IdentifierService:
    return IdentifierService(CaseRepository(db), IdentifierRepository(db))


def get_source_repository(db: Session = Depends(get_db)) -> SourceRepository:
    return SourceRepository(db)

