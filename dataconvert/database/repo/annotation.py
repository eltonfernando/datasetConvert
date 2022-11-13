from typing import List
from sqlalchemy.exc import IntegrityError
from ..tables import TableAnnotation, TableImage, TableBoundbox
from ..connection import DBConnection


class RepAnnotation:

    def __init__(self, connect=DBConnection) -> None:
        self.__connect = connect

    def select(self)-> List[TableAnnotation]:
        with self.__connect() as db:
            data: List[TableAnnotation] = db.session.query(TableAnnotation).all()
            return data

    def select_by_id(self, id) -> List[TableAnnotation]:
        with self.__connect as db:
            data:List[TableAnnotation] = db.session.query(TableAnnotation).filter(
                TableAnnotation.name_image == id
            ).all()
            return data

    def add_all(self, tables: List[TableAnnotation]):
        with self.__connect() as db:
            try:
                db.session.add_all(tables)
                db.session.commit()
            except IntegrityError as error:
                db.session.rollback()

    
    def insert(self, table: TableAnnotation):
        with self.__connect() as db:
            try:
                db.session.add(table)
                db.session.commit()
            except IntegrityError as error:
                db.session.rollback()
            except Exception as error:
                raise error

    def update(self, name_image, new_name):
        with self.__connect() as db:
            db.session.query(TableAnnotation).filter(
                TableAnnotation.name_image==name_image
            ).update({"name_image":new_name})
            db.session.commit()
   
    def delete(self, name_image):
        with self.__connect() as db:
            db.session.query(TableAnnotation).filter(
                TableAnnotation.name_image == name_image
            ).delete()
            db.session.commit()
