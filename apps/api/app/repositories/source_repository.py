from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.entities import SourceMatch, SourceRecord


class SourceRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list_for_case(self, case_id):
        stmt = (
            select(SourceMatch, SourceRecord)
            .join(SourceRecord, SourceRecord.id == SourceMatch.source_record_id)
            .where(SourceMatch.case_id == case_id)
            .order_by(SourceMatch.match_score.desc())
        )
        return self.db.execute(stmt).all()

