from sqlalchemy import Column, String, Integer,MetaData, Table
from ..configs import Base, DBConnection

#def __create_tables():
meta_data = MetaData()
table_anotation = Table(
    "anotation",
    meta_data,
    Column("name_image",String,primary_key = True),
    Column("size_image",String)
)

table_bandbox = Table(
    "bandbox",
    meta_data,
    Column("id",String,nullable=False),
    Column("boxs",String)
)
table_key_point = Table(
    "key_point",
    meta_data,
    Column("id",String),
    Column("points",String)
)
with DBConnection() as db:
    meta_data.create_all(db.get_engine())


class TableAnotation(Base):
    __table__ = table_anotation

def __repr__(self):
        return f"TableAnotation {self.name_image}: {self.bandboxs}: {self.size_image}"


class TableBandbox(Base):
    __table__ = table_bandbox
    def __repr__(self):
        return f"TableBandbox {self.name_image}: {self.bandboxs}: {self.size_image}"
