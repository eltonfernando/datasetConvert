from sqlalchemy import Column, String, Integer, MetaData, Table, ForeignKey, BLOB, Float
import os
from sqlalchemy import create_engine


def create_database():

    meta_data = MetaData()

    table_anotation = Table(
        "annotation",
        meta_data,
        Column("name_image", String, primary_key=True),
    )

    table_images = Table(
        "metadata",
        meta_data,
        Column("name_image", String, ForeignKey("annotation.name_image"),primary_key=True, nullable=True),
        Column("width", Integer, nullable=False),
        Column("height", Integer, nullable=False),
        Column("channel", Integer, nullable=False),
        Column("blob", BLOB),
        
    )
    table_boundbox = Table(
        "boundbox",
        meta_data,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("name_image", String, ForeignKey("annotation.name_image"), nullable=True),
        Column("label", String, nullable=False),
        Column("x_min", Integer, nullable=False),
        Column("y_min", Integer, nullable=False),
        Column("x_max", Integer, nullable=False),
        Column("y_max", Integer, nullable=False),
        Column("confidencie", Float, nullable=False),
    )
    path = "assets/base.db"
    if os.path.isfile(path=path):
        os.remove(path)

    host_engine = os.path.join("sqlite:///"+path)
    engine = create_engine(host_engine)
    meta_data.create_all(engine)


if __name__ == "__main__":
    create_database()
