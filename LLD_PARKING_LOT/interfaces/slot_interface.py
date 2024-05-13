from abc import ABC, abstractmethod

class SlotInterface(ABC):
    def __init__(self,slot_no,type_) -> None:
        super().__init__()
        slot_no = slot_no
        type_ = type_
        status = False
        vehicle = None
        in_time = None

    @abstractmethod
    def assign_vehicle(self):
        pass

    @abstractmethod
    def free_slot(self):
        pass