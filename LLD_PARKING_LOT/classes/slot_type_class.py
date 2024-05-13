from LLD_PARKING_LOT.interfaces.slot_type_interface import SlotTypeInterface


class SlotType(SlotTypeInterface):
    def __init__(self,name,length,width,price) -> None:
        super().__init__()
        name = name
        price = price
        length = length
        width = width
    
    def slot_area(self):
        return self.length*self.width
    
    def price_calculation(self,hours):
        return self.price*hours