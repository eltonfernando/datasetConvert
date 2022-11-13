from dataclasses import dataclass
from sqlalchemy.exc import IntegrityError
from ..tables import TableAnnotation, TableBoundbox
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
        with self.__connect() as data_base:
            data = (
                data_base.session.query(TableBoundbox)
                .join(
                    TableAnnotation,
                    TableBoundbox.name_image == TableBoundbox.name_image,
                )
                .with_entities(
                    TableBoundbox.id,
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

    def insert(self, table: TableBoundbox):
        with self.__connect() as data_base:
            try:
                data_base.session.add(table)
                data_base.session.commit()
            except IntegrityError as error:
                data_base.session.rollback()
                raise error

    def delete(self, id: int) -> None:
        with self.__connect() as data_base:
            data_base.session.query(TableBoundbox).filter(
                TableBoundbox.id == id
            ).delete()
            data_base.session.commit()
