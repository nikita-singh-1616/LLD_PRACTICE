from interfaces.slot_type_interface import SlotTypeInterface


class BikeType(SlotTypeInterface):
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

class CarType(SlotTypeInterface):
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

class TruckType(SlotTypeInterface):
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