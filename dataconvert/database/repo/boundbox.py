from sqlalchemy.exc import IntegrityError
from dataclasses import dataclass
from ..tables import TableAnnotation, TableImage, TableBoundbox
from ..connection import DBConnection

@dataclass
class Boundbox:
    """
    Interface 
    """
    name_image: str
    label: str
    x_min: int
    y_min: int
    x_max: int
    y_max: int
    confidencie: float


class RepBoundbox:
    def __init__(self, connect=DBConnection):
        self.__connect = connect

    def select(self):
        with self.__connect() as db:
            data = (
                db.session.query(TableBoundbox)
                .join(
                    TableAnnotation,
                    TableBoundbox.name_image == TableBoundbox.name_image,
                )
                .with_entities(
                    TableAnnotation.name_image,
                    TableBoundbox.label,
                    TableBoundbox.x_min,
                    TableBoundbox.y_min,
                    TableBoundbox.x_max,
                    TableBoundbox.y_max,
                    TableBoundbox.confidencie,
                )
                .all()
            )
            return data

    def insert(self, boundbox: Boundbox):
        with self.__connect() as db:
            try:
                data_insert = TableBoundbox(
                    name_image=boundbox.name_image,
                    label=boundbox.label,
                    x_min=boundbox.x_min,
                    y_min=boundbox.y_min,
                    x_max=boundbox.x_max,
                    y_max=boundbox.x_max,
                    confidencie=boundbox.confidencie,
                )
                db.session.add(data_insert)
                db.session.commit()
            except Exception as error:
                db.session.rollback()
                raise error
