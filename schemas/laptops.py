import datetime

from pydantic import BaseModel, Field
from db import SessionLocal

db = SessionLocal()


class CreateLaptop(BaseModel):
    category_id: int = Field(..., gt=0)
    name: str
    brend: str
    model: str
    processor: str
    ram: int = Field(..., gt=0)
    rom: int = Field(..., gt=0)
    rom_type: str
    color: str
    screen_diagonal: float = Field(..., gt=0)
    screen_refresh: int = Field(..., gt=0)
    videocard: str
    cores: int = Field(..., gt=0)
    weight: int = Field(..., gt=0)
    year: int = Field(..., gt=0)
    country: str
    price: int = Field(..., gt=0)
    discount: int
    discount_time: datetime.date
    count: int = Field(..., gt=0)


class UpdateLaptop(BaseModel):
    ident: int = Field(..., gt=0)
    category_id: int = Field(..., gt=0)
    name: str
    brend: str
    model: str
    processor: str
    ram: int = Field(..., gt=0)
    rom: int = Field(..., gt=0)
    rom_type: str
    color: str
    screen_diagonal: float = Field(..., gt=0)
    screen_refresh: int = Field(..., gt=0)
    videocard: str
    cores: int = Field(..., gt=0)
    weight: int = Field(..., gt=0)
    year: int = Field(..., gt=0)
    country: str
    price: int = Field(..., gt=0)
    discount: int
    discount_time: datetime.date
    count: int = Field(..., gt=0)
