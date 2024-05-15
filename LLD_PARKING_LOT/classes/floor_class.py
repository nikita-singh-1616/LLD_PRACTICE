
from classes.slot_class import Slot
from interfaces.floor_interface import FloorInterface
from interfaces.slot_type_interface import SlotFactory


class Floor(FloorInterface):
    def __init__(self, floor_no,no_of_slots,slot_factory) -> None:
        super().__init__(floor_no,no_of_slots)
        self.slot_factory = slot_factory
        self.add_slots()

    def add_slots(self):
        for i in range(self.no_of_slots):
            if i == 0:
                slot_type = self.slot_factory.slot_factory('Truck')
            elif i == 1 or i == 2:
                slot_type = self.slot_factory.slot_factory('Bike')
            else:
                slot_type = self.slot_factory.slot_factory('Car')
            self.slots.append(Slot(i+1,slot_type))
        print('Floor is ready')

    def find_available_slot(self,vehicle):
        for i in self.slots:
            if i.is_vehicle_type(vehicle) and i.is_available():
                slot_no = i.park(vehicle)
                return str(self.floor_no)+'_'+str(slot_no)
        return ''

    def find_slot(self,slot):
        slot = self.slots[slot-1]
        if not slot.is_available():
            slot.free_slot()
        else:
            return -1

    def display(self):
        pass





        # while True:
        #     print('Assign the number of slots in each slot type')
        #     if input('press exit to exit') == 'exit':
        #         return False
        #     type_to_qty = {}
        #     for i in self.slot_types:
        #         qty = int(input(f'Enter the number of slots of slot type {i.name}'))
        #         type_to_qty[i] = qty*i.get_area()
        #     if sum(type_to_qty.values())<total_area:
        #         if input('there is some space left press ok to continue') == 'ok':
        #             break
        #     elif sum(type_to_qty.values())<total_area:
        #         break
        #     else:
        #         print('total area is greater than parking lot area try again ')
        # print('Building Floor')
        # for i in self.slot_types:
        #     self.slots[i] = []
        #     for j in type_to_qty[i]:
        #         self.slots[i].append(Slot(i.name+str(j),i))
        # print('Floor built successfully')

