
from LLD_PARKING_LOT.classes.slot_class import Slot
from LLD_PARKING_LOT.interfaces.floor_interface import FloorInterface


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
            if i.is_vehicle_type(vehicle.type_) and i.is_available():
                slot_no = i.park(vehicle)
                return str(self.floor_no)+'_'+str(slot_no)
        return ''

    def find_slot(self,slot):
        slot = self.slots[slot-1]
        if not slot.is_available():
            price = slot.free_slot()
            return price
        else:
            return -1

    def display(self,vehicle_type,display_type):
        ans = []
        if display_type == 'free slots':
            for i in self.slots:
                if i.is_vehicle_type(vehicle_type) and i.is_available():
                    ans.append(i.slot_no)
        elif display_type == 'occupied slots':
            for i in self.slots:
                if i.is_vehicle_type(vehicle_type) and not i.is_available():
                    ans.append(i.slot_no)
        print(f'{self.floor_no}:{ans}')


