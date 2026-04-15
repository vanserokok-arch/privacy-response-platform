from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class IdentifierCreate(BaseModel):
    kind: str
    value: str
    confidence: float = 0.9


class IdentifierRead(BaseModel):
    id: UUID
    case_id: UUID
    kind: str
    value: str
    confidence: float
    created_at: datetime

    model_config = {"from_attributes": True}

