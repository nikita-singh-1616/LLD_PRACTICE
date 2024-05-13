from abc import ABC

class VehicleInterface(ABC):
    def __init__(self,type_,reg_no,color) -> None:
        super().__init__()
        type_ = type_
        reg_no = reg_no
        color = color

