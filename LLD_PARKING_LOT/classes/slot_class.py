
import datetime
from interfaces.slot_interface import SlotInterface


class Slot(SlotInterface):
    def __init__(self, slot_no, type_) -> None:
        super().__init__(slot_no, type_)

    def park(self,vehicle_obj):
        self.status = True
        self.vehicle = vehicle_obj
        self.in_time = datetime.datetime.now()
        print('Vehicle Parked Successfully')
        return self.slot_no

    def free_slot(self):
        self.status = False
        self.vehicle = None
        price = self.type_.price_calculation((datetime.datetime.now()-self.in_time).total_seconds() / 3600)
        print('Vehicle Unparked Successfully')
        return price

    def is_available(self):
        return not self.status
    
    def is_vehicle_type(self,vehicle):
        return vehicle.type_ == self.type_.name