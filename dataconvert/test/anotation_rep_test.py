from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from ..tables import TableAnotation
from ..repository import AnotationRepo


class ConnectionHandlerMock:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [
                        mock.call.query(TableAnotation),
                        mock.call.filter(TableAnotation.name_image == "xxx.jpg"),
                    ],
                    [
                        TableAnotation(
                            name_image="xxx.jpg",
                            bandboxs="",
                            size_image="(10,20)",
                            key_point="[[x,y]]",
                        )
                    ],
                )
            ]
        )


def tes_select():
    result = AnotationRepo(ConnectionHandlerMock)
    response = result.select()
    print(response)
