from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.entities import Identifier
from app.schemas.identifier import IdentifierCreate


class IdentifierRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, case_id, payload: IdentifierCreate) -> Identifier:
        identifier = Identifier(case_id=case_id, **payload.model_dump())
        self.db.add(identifier)
        self.db.commit()
        self.db.refresh(identifier)
        return identifier

    def list_for_case(self, case_id) -> list[Identifier]:
        stmt = select(Identifier).where(Identifier.case_id == case_id).order_by(Identifier.created_at.desc())
        return list(self.db.scalars(stmt))

