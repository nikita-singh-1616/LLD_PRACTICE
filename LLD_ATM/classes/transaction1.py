import datetime
from intefaces.transaction_interface import transactionInterface


class Transaction1(transactionInterface):
    def __init__(self) -> None:
        super().__init__()
        self.type = None

    def create_transaction(self,type,amount,from_,to):
        self.type = type
        self.amount = amount
        self.date = datetime.datetime.now()
        self.from_account = from_
        self.to_account = to

    def display_transaction(self):
        print(f'{self.type}\t{self.amount}\t{self.date}\t{self.from_account}\t{self.to_account}')
        