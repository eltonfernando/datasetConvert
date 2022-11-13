from sqlalchemy import Column, String, Integer, ForeignKey, BLOB, Float
from sqlalchemy.orm import relationship
from .base import Base


class TableAnnotation(Base):
    __tablename__ = "annotation"

    name_image = Column(String, primary_key=True)
    children_image = relationship("TableImage", back_populates="parent")
    children_boundbox = relationship("TableBoundbox", back_populates="parent")

    def __init__(self, name_image, children_image=None, children_boundbox=None):
        self.name_image = name_image
        self.children_boundbox = children_boundbox
        self.children_image = children_image

    def __repr__(self):
        return f"TableAnnotation {self.name_image}"


class TableBoundbox(Base):
    __tablename__ = "boundbox"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_image = Column(String, ForeignKey(TableAnnotation.name_image), nullable=False)
    parent = relationship("TableAnnotation", back_populates="children_boundbox")
    label = Column(String, nullable=False)
    x_min = Column(String, nullable=False)
    y_min = Column(String, nullable=False)
    x_max = Column(String, nullable=False)
    y_max = Column(String, nullable=False)
    confidencie = Column(Float, nullable=False)

    def __init__(self, label, x_min, y_min, x_max, y_max, confidencie):
        self.label = label
        self.x_min = x_min
        self.y_min = y_min
        self.y_max = y_max
        self.x_max = x_max
        self.confidencie = confidencie

    def __repr__(self):
        return f"TableImage {self.id}: {self.name_image}: {self.label}: {self.x_min}: {self.y_min}"


class TableImage(Base):
    __tablename__ = "metadata"
    name_image = Column(
        String, ForeignKey("annotation.name_image"), primary_key=True, nullable=False
    )
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    channel = Column(Integer, nullable=False)
    blob = Column(BLOB)

    parent = relationship("TableAnnotation", back_populates="children_image")

    def __init__(self, width, height, channel, blob):
        self.width = width
        self.height = height
        self.channel = channel
        self.blob = blob

    def __repr__(self):
        return f"TableImage {self.id}:{self.name_image} :{self.width}: {self.heigth}: {self.channel}"
