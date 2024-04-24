from db import Base
from sqlalchemy import Column, String, Integer, Float, Date


class Laptops(Base):
    __tablename__ = 'laptops'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    brend = Column(String(255), nullable=False)
    model = Column(String(255), nullable=False)
    processor = Column(String(255), nullable=False)
    ram = Column(Integer, nullable=False)
    rom = Column(Integer, nullable=False)
    rom_type = Column(String(255), nullable=False)
    color = Column(String(255), nullable=False)
    screen_diagonal = Column(Float, nullable=False)
    screen_refresh = Column(Integer, nullable=False)
    videocard = Column(String(255), nullable=True)
    cores = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    country = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    discount = Column(Integer, nullable=True)
    discount_price = Column(Integer, nullable=False)
    discount_time = Column(Date)
    count = Column(Integer, nullable=True)
    source_name = Column(String(255), nullable=False)
    view = Column(Integer)
    favorites = Column(Integer)

