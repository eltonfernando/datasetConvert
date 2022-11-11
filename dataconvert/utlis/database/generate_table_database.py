from sqlalchemy import Column, String, Integer, MetaData, Table, ForeignKey, BLOB, Float
import os
from sqlalchemy import create_engine


def create_database():

    meta_data = MetaData()

    table_anotation = Table(
        "anotation",
        meta_data,
        Column("name_image", String, primary_key=True),
    )

    table_images = Table(
        "bytes_image",
        meta_data,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("width", Integer, nullable=False),
        Column("height", Integer, nullable=False),
        Column("channel", Integer, nullable=False),
        Column("blob_image", BLOB),
        Column("name_image", String, ForeignKey("anotation.name_image"), nullable=True),
    )
    table_boundbox = Table(
        "boundbox",
        meta_data,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("name_image", String, ForeignKey("anotation.name_image"), nullable=True),
        Column("label", String, nullable=False),
        Column("x_min", Integer, nullable=False),
        Column("y_min", Integer, nullable=False),
        Column("x_max", Integer, nullable=False),
        Column("y_max", Integer, nullable=False),
        Column("confidencie", Float, nullable=False),
    )

    host_engine = os.path.join("sqlite:///db.db")
    engine = create_engine(host_engine)
    meta_data.create_all(engine)


if __name__ == "__main__":
    create_database()
