from pydantic import BaseModel, Field


class CreateLikes(BaseModel):
    source: str
    source_id: int = Field(..., gt=0)
