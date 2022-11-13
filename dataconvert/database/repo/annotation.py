from typing import List
from sqlalchemy.exc import IntegrityError
from ..tables import TableAnnotation
from ..connection import DBConnection


class RepAnnotation:
    def __init__(self, connect=DBConnection) -> None:
        self.__connect = connect

    def select(self) -> List[TableAnnotation]:
        with self.__connect() as data_base:
            data: List[TableAnnotation] = data_base.session.query(TableAnnotation).all()
            return data

    def select_by_id(self, id) -> List[TableAnnotation]:
        with self.__connect as data_base:
            data: List[TableAnnotation] = (
                data_base.session.query(TableAnnotation)
                .filter(TableAnnotation.name_image == id)
                .all()
            )
            return data

    def add_all(self, tables: List[TableAnnotation]):
        with self.__connect() as data_base:
            try:
                data_base.session.add_all(tables)
                data_base.session.commit()
            except IntegrityError as error:
                print(error)
                data_base.session.rollback()

    def insert(self, table: TableAnnotation):
        with self.__connect() as data_base:
            try:
                data_base.session.add(table)
                data_base.session.commit()
            except IntegrityError as error:
                data_base.session.rollback()
            except Exception as error:
                raise error

    def update(self, name_image, new_name):
        with self.__connect() as data_base:
            data_base.session.query(TableAnnotation).filter(
                TableAnnotation.name_image == name_image
            ).update({"name_image": new_name})
            data_base.session.commit()

    def delete(self, name_image):
        with self.__connect() as data_base:
            data_base.session.query(TableAnnotation).filter(
                TableAnnotation.name_image == name_image
            ).delete()
            data_base.session.commit()
