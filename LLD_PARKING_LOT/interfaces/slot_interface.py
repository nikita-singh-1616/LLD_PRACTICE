from abc import ABC, abstractmethod

class SlotInterface(ABC):
    def __init__(self,slot_no,type_) -> None:
        super().__init__()
        self.slot_no = slot_no
        self.type_ = type_
        self.status = False
        self.vehicle = None
        self.in_time = None

    @abstractmethod
    def park(self,vehicle_obj):
        pass

    @abstractmethod
    def free_slot(self):
        pass