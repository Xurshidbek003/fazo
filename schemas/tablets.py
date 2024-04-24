import datetime

from pydantic import BaseModel, Field


class CreateTablet(BaseModel):
    category_id: int = Field(..., gt=0)
    name: str
    brend: str
    model: str
    ram: int = Field(..., gt=0)
    rom: int = Field(..., gt=0)
    color: str
    battery: int = Field(..., gt=0)
    screen_diagonal: float = Field(..., gt=0)
    screen_refresh: int = Field(..., gt=0)
    camera: int = Field(..., gt=0)
    self_camera: int = Field(..., gt=0)
    year: int = Field(..., gt=0)
    weight: int = Field(..., gt=0)
    country: str
    price: int = Field(..., gt=0)
    discount: int
    discount_time: datetime.date
    count: int = Field(..., gt=0)


class UpdateTablet(BaseModel):
    ident: int = Field(..., gt=0)
    category_id: int = Field(..., gt=0)
    name: str
    brend: str
    model: str
    ram: int = Field(..., gt=0)
    rom: int = Field(..., gt=0)
    color: str
    battery: int = Field(..., gt=0)
    screen_diagonal: float = Field(..., gt=0)
    screen_refresh: int = Field(..., gt=0)
    camera: int = Field(..., gt=0)
    self_camera: int = Field(..., gt=0)
    year: int = Field(..., gt=0)
    weight: int = Field(..., gt=0)
    country: str
    price: int = Field(..., gt=0)
    discount: int
    discount_time: datetime.date
    count: int = Field(..., gt=0)
