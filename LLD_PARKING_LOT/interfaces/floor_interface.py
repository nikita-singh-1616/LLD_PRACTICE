from abc import ABC, abstractmethod

class FloorInterface(ABC):
    def __init__(self,floor_no,slot_types) -> None:
        super().__init__()
        floor_no = floor_no
        slot_types = slot_types
        slots = {}
        
    @abstractmethod
    def find_available_slot(self):
        pass

    @abstractmethod
    def add_slots(self):
        pass

    @abstractmethod
    def display(self):
        pass