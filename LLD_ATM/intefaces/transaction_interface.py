from abc import ABC, abstractmethod


class transactionInterface(ABC):
    def __init__(self) -> None:
        self.type = None
        self.amount = None
        self.date = None
        self.from_account = None
        self.to_account = None

    @abstractmethod
    def create_transaction(self):
        pass

    @abstractmethod
    def display_transaction(self):
        pass