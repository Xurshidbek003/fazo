from pydantic import BaseModel, Field


class CreateCarts(BaseModel):
    source: str
    source_id: int = Field(..., gt=0)
