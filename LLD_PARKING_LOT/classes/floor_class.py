
from LLD_PARKING_LOT.classes.slot_class import Slot
from LLD_PARKING_LOT.interfaces.floor_interface import FloorInterface


class Floor(FloorInterface):
    def __init__(self, floor_no, slot_types) -> None:
        super().__init__(floor_no, slot_types)

    def add_slots(self,total_area):
        while True:
            print('Assign the number of slots in each slot type')
            if input('press exit to exit') == 'exit':
                return False
            type_to_qty = {}
            for i in self.slot_types:
                qty = int(input(f'Enter the number of slots of slot type {i.name}'))
                type_to_qty[i] = qty*i.get_area()
            if sum(type_to_qty.values())<total_area:
                if input('there is some space left press ok to continue') == 'ok':
                    break
            elif sum(type_to_qty.values())<total_area:
                break
            else:
                print('total area is greater than parking lot area try again ')
        print('Building Floor')
        for i in self.slot_types:
            self.slots[i] = []
            for j in type_to_qty[i]:
                self.slots[i].append(Slot(i.name+str(j),i))
        print('Floor built successfully')

