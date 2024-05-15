from abc import ABC

class VehicleInterface(ABC):
    def __init__(self,type_,reg_no,color) -> None:
        super().__init__()
        self.type_ = type_
        self.reg_no = reg_no
        self.color = color

