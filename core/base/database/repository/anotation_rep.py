from ..configs.connection import DBConnection
from ..tables import TableAnotation

class AnotationRepo:
    def __init__(self,connect):
        self.__connect = connect

    def select(self):
        with self.__connect() as db:
            data = db.session.query(TableAnotation).all()
            return data

    def insert(self,name_image,bandboxs,size_image,key_point):
        with self.__connect() as db:
            try:
                data_insert = TableAnotation(
                    name_image=name_image,
                    bandboxs=bandboxs,
                    size_image=size_image,
                    key_point=key_point)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as error:
                db.session.rollback()
                raise error
    
    def delete(self,name_image):
        with self.__connect() as db:
            db.session.query(AnotationRepo).filter(AnotationRepo.name_image==name_image).delete()
            db.session.commit()
    


