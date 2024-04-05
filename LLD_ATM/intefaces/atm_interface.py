from abc import ABC, abstractmethod


class ATM(ABC):
    def __init__(self):
        self.current_user = None
        self.card_no = None
        self.card = None

    @abstractmethod
    def enter_card_no(self):
        pass
