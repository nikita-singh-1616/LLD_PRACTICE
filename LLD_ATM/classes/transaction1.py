import datetime
from intefaces.transaction_interface import transactionInterface


class Transaction1(transactionInterface):
    def __init__(self) -> None:
        super().__init__()
        self.type = None

    def create_transaction(self,type,amount):
        self.type = type
        self.amount = amount
        self.date = datetime.datetime.now()

    def display_transaction(self):
        print(f'{self.type}\t{self.amount}\t{self.date}')
        