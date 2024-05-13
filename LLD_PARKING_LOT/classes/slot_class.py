
import datetime
from LLD_PARKING_LOT.interfaces.slot_interface import SlotInterface


class Slot(SlotInterface):
    def __init__(self, slot_no, type_) -> None:
        super().__init__(slot_no, type_)

    def assign_vehicle(self,vehicle_obj):
        self.status = True
        self.vehicle = vehicle_obj
        self.in_time = datetime.datetime.now()
        print('Vehicle Parked Successfully')

    def free_slot(self):
        self.status = False
        self.vehicle = None
        print('Vehicle Unparked Successfully')

    def is_available(self):
        return self.status
    
    def get_slot_no(self):
        return self.slot_no