from uuid import UUID

from app.exceptions.http import not_found
from app.repositories.case_repository import CaseRepository
from app.schemas.case import CaseCreate


class CaseService:
    def __init__(self, repo: CaseRepository) -> None:
        self.repo = repo

    def create(self, payload: CaseCreate):
        return self.repo.create(payload)

    def list(self):
        return self.repo.list()

    def get(self, case_id: UUID):
        case = self.repo.get(case_id)
        if not case:
            raise not_found(f"Case {case_id} not found")
        return case

