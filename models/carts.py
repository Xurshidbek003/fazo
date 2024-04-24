from sqlalchemy.orm import relationship, backref
from db import Base
from sqlalchemy import Column, String, Integer, and_, Boolean
from models.laptops import Laptops
from models.tablets import Tablets
from models.phones import Phones
from models.users import Users


class Carts(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    source = Column(String(255), nullable=False)
    source_id = Column(Integer, nullable=False)
    product_count = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False)

    users = relationship("Users", foreign_keys=[user_id],
                         primaryjoin=lambda: Users.id == Carts.user_id)

    laptop = relationship("Laptops", foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Laptops.id == Carts.source_id, Carts.source == "laptop"),
                          backref=backref("carts"))

    phone = relationship("Phones", foreign_keys=[source_id],
                         primaryjoin=lambda: and_(Phones.id == Carts.source_id, Carts.source == "phone"),
                         backref=backref("carts"))

    tablet = relationship("Tablets", foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Tablets.id == Carts.source_id, Carts.source == "tablet"),
                          backref=backref("carts"))
