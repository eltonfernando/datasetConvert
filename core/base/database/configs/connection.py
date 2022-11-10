import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection():
    
    def __init__(self) -> None:
        self.__path= ""
        self.__host_engine = os.path.join("sqlite:///db.db")
        self.__engine =self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        return create_engine(self.__host_engine)

    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.session.close()