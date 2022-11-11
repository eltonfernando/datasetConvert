from sqlalchemy.exc import IntegrityError
from ..tables import TableAnnotation, TableImage, TableBoundbox
from ..connection import DBConnection


class RepImage:
    def __init__(self, connect=DBConnection):
        self.__connect = connect

    def select_image(self, name_image) -> bytes:
        with self.__connect as db:
            data = (
                db.session.query(TableImage)
                .filter(TableImage.name_image == name_image)
                .select()
            )
            return data

    def select(self):
        with self.__connect() as db:
            data = (
                db.session.query(TableImage)
                .join(
                    TableAnnotation, TableImage.name_image == TableAnnotation.name_image
                )
                .with_entities(
                    TableAnnotation.name_image, TableImage.size, TableImage.blob
                )
                .all()
            )
            return data

    def insert(self, name_image, blob_image):
        with self.__connect() as db:
            try:
                data_insert = TableImage(name_image=name_image, blob_image=blob_image)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as error:
                db.session.rollback()
                raise error
