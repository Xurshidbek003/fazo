from db import Base
from sqlalchemy import Column, String, Integer, and_
from sqlalchemy.orm import relationship, backref
from models.laptops import Laptops
from models.phones import Phones
from models.tablets import Tablets


class Files(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String(255), nullable=False)
    source_id = Column(Integer, nullable=False)
    file = Column(String(255), nullable=False)

    laptop = relationship("Laptops", foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Laptops.id == Files.source_id, Files.source == "laptop"),
                          backref=backref("files"))

    phone = relationship("Phones", foreign_keys=[source_id],
                         primaryjoin=lambda: and_(Phones.id == Files.source_id, Files.source == "phone"),
                         backref=backref("files"))

    tablet = relationship("Tablets", foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Tablets.id == Files.source_id, Files.source == "tablet"),
                          backref=backref("files"))
