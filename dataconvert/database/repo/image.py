from sqlalchemy.exc import IntegrityError
from dataclasses import dataclass
from ..tables import TableAnnotation, TableImage, TableBoundbox
from ..connection import DBConnection

@dataclass
class MetadataImage:
    name_image: str
    width: int
    height: int
    channel: int
    blob: bytes
    
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
                    TableAnnotation.name_image, 
                    TableImage.width,
                    TableImage.height,
                    TableImage.channel,
                    TableImage.blob
                )
                .all()
            )
            return data

    def insert(self,data_image: TableImage):
        with self.__connect() as db:
            try:
                db.session.add(data_image)
                db.session.commit()
            except Exception as error:
                db.session.rollback()
                raise error
    def delete(self,id: int)-> None:
        with self.__connect() as db:
            db.session.query(TableImage).filter(
                TableImage.id == id
            ).delete()
            db.session.commit()
