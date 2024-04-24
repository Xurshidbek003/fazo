from db import Base
from sqlalchemy import Column, Integer, Date


class Buys(Base):
    __tablename__ = 'buys'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    buy_date = Column(Date, nullable=False)

