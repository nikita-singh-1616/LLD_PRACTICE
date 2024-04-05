from abc import ABC, abstractmethod


class BankInterface(ABC):
    def __init__(self):
        self.accounts = {}
        self.card_accounts = {}
        
    @abstractmethod
    def search_account_from_account_number(self,account_no):
        pass

    @abstractmethod
    def search_account_from_card_number(self,card_no):
        pass

    @abstractmethod
    def create_account(self):
        pass

    @abstractmethod
    def create_card(self):
        pass

