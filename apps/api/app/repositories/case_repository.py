from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.entities import Case
from app.schemas.case import CaseCreate


class CaseRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, payload: CaseCreate) -> Case:
        case = Case(**payload.model_dump())
        self.db.add(case)
        self.db.commit()
        self.db.refresh(case)
        return case

    def list(self) -> list[Case]:
        return list(self.db.scalars(select(Case).order_by(Case.created_at.desc())))

    def get(self, case_id: UUID) -> Case | None:
        return self.db.get(Case, case_id)

