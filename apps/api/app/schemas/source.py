from uuid import UUID

from pydantic import BaseModel


class SourceRecordRead(BaseModel):
    source_record_id: UUID
    domain: str
    url: str
    source_type: str
    match_score: float

