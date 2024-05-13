from LLD_PARKING_LOT.classes.slot_type_class import SlotType


class ParkingLot():
    def __init__(self,length,width,name) -> None:
        length = length
        width = width
        name = name
        floors = []
        slot_types = []
    
    def get_info(self):
        slot_types_no = int(print('enter the no. of types of vehicles you want in your lot '))
        for i in range(slot_types_no):
            name = input('name of the type of vehicle ')
            length = input('length of slot to assign to the vehicle ')
            width = input('width of slot to assign to the vehicle ')
            price = input('price of slot to assign to the vehicle ')
            self.slot_types.append(SlotType(name,length,width,price))
        floor_nos = int(input('enter the number of floors'))
        for i in floor_nos:
            self.floors.append()

