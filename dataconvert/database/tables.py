from sqlalchemy import Column, String, Integer, MetaData, Table, ForeignKey, BLOB, Float
from sqlalchemy.orm import relationship
from .base import Base
from .connection import DBConnection


class TableAnnotation(Base):
    __tablename__ = "anotation"

    name_image = Column(String, primary_key=True)
    image = relationship("TableImage", backref="image", lazy="subquery")
    boundbox = relationship("TableBoundbox", backref="boundbox", lazy="subquery")

    def __repr__(self):
        return f"TableAnnotation {self.name_image}"


class TableBoundbox(Base):
    __tablename__ = "boundbox"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_image = Column(String, ForeignKey(TableAnnotation.name_image), nullable=False)
    label = Column(String, nullable=False)
    x_min = Column(String, nullable=False)
    y_min = Column(String, nullable=False)
    x_max = Column(String, nullable=False)
    y_max = Column(String, nullable=False)
    confidencie = Column(Float, nullable=False)
    

    def __repr__(self):
        return f"TableImage {self.id}: {self.name_image}: {self.label}: {self.x_min}: {self.y_min}"


class TableImage(Base):
    __tablename__ = "image"
    id = Column(Integer, primary_key=True, autoincrement=True)
    width = Column(Integer, nullable=False)
    heigth = Column(Integer, nullable=False)
    channel = Column(Integer, nullable=False)
    name_image = Column(String, ForeignKey("anotation.name_image"), nullable=False)

    def __init__(self,name_image, width,heigth,channel):
        self.name_image = name_image
        self.width = width
        self.heigth  = heigth
        self.channel = channel

    def __repr__(self):
        return f"TableImage {self.id}: {self.name_image}: {self.width}: {self.heigth}: {self.channel}"
