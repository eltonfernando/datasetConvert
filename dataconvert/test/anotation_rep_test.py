from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from dataconvert.database import TableAnnotation, RepAnnotation



class ConnectionHandlerMock:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [
                        mock.call.query(TableAnnotation),
                        mock.call.filter(TableAnnotation.name_image == "teste"),
                    ],
                    [
                        TableAnnotation(name_image="xxx.jpg"),
                        TableAnnotation(name_image="teste"),
                    ],
                )
            ]
        )
    def __enter__(self):
        #session_make = sessionmaker(bind=self.__engine)
        #self.session = session_make()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


def test_select():
    result = RepAnnotation(ConnectionHandlerMock)
    response = result.select()
    print(response)
