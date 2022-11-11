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
                        mock.call.filter(TableAnnotation.name_image == "xxx.jpg"),
                    ],
                    [
                        TableAnnotation(
                            name_image="xxx.jpg",
                            bandboxs="",
                            size_image="(10,20)",
                            key_point="[[x,y]]",
                        )
                    ],
                )
            ]
        )


def tess_select():
    result = RepAnnotation(ConnectionHandlerMock)
    response = result.select()
    print(response)
