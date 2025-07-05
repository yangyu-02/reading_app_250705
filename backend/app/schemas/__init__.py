from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BaseSchema(BaseModel):
    model_config = {"from_attributes": True}


class TimestampSchema(BaseSchema):
    created_at: datetime
    updated_at: Optional[datetime] = None