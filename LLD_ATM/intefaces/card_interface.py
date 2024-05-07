from abc import ABC, abstractmethod


class CardInterface(ABC):
    def __init__(self) -> None:
        self.card_no = None
        self.pin = None
        self.bank = None
        self.expiry_date = None
        self.status = False

    @abstractmethod
    def create_card(self):
        pass

    @abstractmethod
    def validate_card(self):
        pass