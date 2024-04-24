from pydantic import BaseModel


class CreateCategories(BaseModel):
    name: str


class UpdateCategories(BaseModel):
    ident: int
    name: str
