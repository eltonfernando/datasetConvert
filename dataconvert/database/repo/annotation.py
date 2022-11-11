from sqlalchemy.exc import IntegrityError
from ..tables import TableAnnotation, TableImage, TableBoundbox
from ..connection import DBConnection


class RepAnnotation:
    def __init__(self, connect=DBConnection):
        self.__connect = connect

    def select(self):
        with self.__connect() as db:
            data = db.session.query(TableAnnotation).all()
            return data

    def select_with_box(self):
        pass

    def select_with_point(self):
        pass

    def insert(self, name_image):
        with self.__connect() as db:
            try:
                data_insert = TableAnnotation(name_image=name_image)
                db.session.add(data_insert)
                db.session.commit()
            except IntegrityError as error:
                db.session.rollback()
            except Exception as error:
                raise error

    def delete(self, name_image):
        with self.__connect() as db:
            db.session.query(RepAnnotation).filter(
                RepAnnotation.name_image == name_image
            ).delete()
            db.session.commit()
