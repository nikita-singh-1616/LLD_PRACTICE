from abc import ABC, abstractmethod


class transactionInterface(ABC):
    def __init__(self) -> None:
        self.type = None
        self.amount = None
        self.date = None

    @abstractmethod
    def create_transaction(self):
        pass

    @abstractmethod
    def display_transaction(self):
        pass