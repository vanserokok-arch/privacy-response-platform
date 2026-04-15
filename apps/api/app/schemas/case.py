from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.models.entities import CaseStatus


class CaseCreate(BaseModel):
    owner_id: UUID
    title: str
    jurisdiction: str = "RU"


class CaseRead(BaseModel):
    id: UUID
    owner_id: UUID
    title: str
    status: CaseStatus
    jurisdiction: str
    created_at: datetime

    model_config = {"from_attributes": True}

