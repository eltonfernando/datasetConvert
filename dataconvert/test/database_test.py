import shutil
import os
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dataconvert.database import RepAnnotation
from dataconvert.database.tables import TableImage, TableBoundbox, TableAnnotation


shutil.copy("assets/base.db", "test.db")


class DBConnectionTest:
    """
    manage datadase connection

    mysql+oursql://<user>:<password>@<host>[:<port>]/<dbname>
    postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase

    see in utils/database on how to create the tables

    """

    def __init__(self) -> None:
        self.__host_engine = os.path.join("sqlite:///test.db")
        self.__engine = create_engine(self.__host_engine)
        self.session = None

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


def test_add_all():
    image_name = "image01.jpg"
    input_table: List[TableAnnotation] = [
        TableAnnotation(
            name_image=image_name,
            children_boundbox=[
                TableBoundbox(
                    label="teste 01",
                    x_min=0,
                    y_min=0,
                    x_max=20,
                    y_max=20,
                    confidencie=0.7,
                ),
                TableBoundbox(
                    label="teste 02",
                    x_min=3,
                    y_min=3,
                    x_max=40,
                    y_max=40,
                    confidencie=0.95,
                ),
            ],
            children_image=[
                TableImage(
                    width=300, height=400, channel=3, blob=bytearray(b"\btestasll")
                )
            ],
        )
    ]
    repro = RepAnnotation(DBConnectionTest)
    repro.add_all(input_table)


def test_insert():

    input_data = TableAnnotation(
        name_image="test_insert.jpg",
        children_boundbox=[
            TableBoundbox(
                label="test", y_min=0, x_min=0, x_max=50, y_max=100, confidencie=0.6
            )
        ],
        children_image=[
            TableImage(
                width=320, height=480, channel=3, blob=bytearray(b"\bldfdsadfadff")
            )
        ],
    )

    repro = RepAnnotation(DBConnectionTest)
    repro.insert(input_data)

    print(repro.select())
