from abc import ABC, abstractmethod

class FloorInterface(ABC):
    def __init__(self,floor_no,no_of_slots) -> None:
        super().__init__()
        self.floor_no = floor_no
        self.no_of_slots = no_of_slots
        self.slots = []
        
    @abstractmethod
    def find_available_slot(self):
        pass

    @abstractmethod
    def add_slots(self):
        pass

    @abstractmethod
    def display(self):
        pass