from abc import ABC, abstractmethod


class AccountInterface(ABC):
    def __init__(self):
        self.account_number = None
        self.user = None
        self.amount = None 
        self.account_type = None
        self.transaction_history = {}

    @abstractmethod
    def create_transaction(self):
        pass

    @abstractmethod
    def update_amount(self):
        pass

    @abstractmethod
    def display_amount(self):
        pass

    @abstractmethod
    def display_transactions(self):
        pass
    
