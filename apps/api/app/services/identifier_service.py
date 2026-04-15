from app.repositories.case_repository import CaseRepository
from app.repositories.identifier_repository import IdentifierRepository
from app.schemas.identifier import IdentifierCreate


class IdentifierService:
    def __init__(self, case_repo: CaseRepository, identifier_repo: IdentifierRepository) -> None:
        self.case_repo = case_repo
        self.identifier_repo = identifier_repo

    def create_for_case(self, case_id, payload: IdentifierCreate):
        if not self.case_repo.get(case_id):
            from app.exceptions.http import not_found

            raise not_found(f"Case {case_id} not found")
        return self.identifier_repo.create(case_id, payload)

