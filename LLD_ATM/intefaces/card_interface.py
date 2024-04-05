from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self) -> None:
        self.card_no = None
        self.pin = None
        self.bank = None
        self.expiry_date = None

    @abstractmethod
    def create_card(self):
        pass

    @abstractmethod
    def validate_card(self):
        pass