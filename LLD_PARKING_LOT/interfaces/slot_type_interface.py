from abc import ABC, abstractmethod

class SlotTypeInterface(ABC):
    def __init__(self,name,length,width,price) -> None:
        super().__init__()
        name = name
        price = price
        length = length
        width = width
    @abstractmethod
    def slot_area(self):
        pass
    @abstractmethod
    def price_calculation(self,hours):
        pass