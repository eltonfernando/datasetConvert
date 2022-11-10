

from typing import List

class IBandbox:
    x_min: int 
    y_min: int
    x_max: int
    y_max: int
    label: str

class IAnotationBandboxs:
    bandbox: List[IBandbox]

class IKpoint:
    x: int
    y: int