from abc import ABC, abstractmethod


class ATMInterface(ABC):
    def __init__(self):
        self.current_account = None
        self.card_no = None
        self.card = None
        self.banks = None

    @abstractmethod
    def enter_card_no(self):
        pass
