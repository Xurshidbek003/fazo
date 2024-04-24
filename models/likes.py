from sqlalchemy.orm import backref, relationship

from db import Base
from sqlalchemy import Column, String, Integer, and_

from models.laptops import Laptops
from models.tablets import Tablets
from models.phones import Phones
from models.users import Users


class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    source = Column(String(255), nullable=False)
    source_id = Column(Integer, nullable=False)

    user = relationship("Users", foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == Likes.user_id)

    laptop = relationship("Laptops", foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Laptops.id == Likes.source_id, Likes.source == "laptop"),
                          backref=backref("likes"))

    phone = relationship("Phones", foreign_keys=[source_id],
                         primaryjoin=lambda: and_(Phones.id == Likes.source_id, Likes.source == "phone"),
                         backref=backref("likes"))

    tablet = relationship("Tablets", foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Tablets.id == Likes.source_id, Likes.source == "tablet"),
                          backref=backref("likes"))
