import datetime
from intefaces.account_interface import AccountInterface


class Bank1Account(AccountInterface):
    def __init__(self):
        super().__init__()
        self.user = None

    def autogenerate_account_number(self):
        self.account_number=str(datetime.datetime.now().microsecond)+'__'+self.user.get_user_specific_details('date_of_birth')
        print(self.account_number)

    def create_account(self,user):
        self.user = user
        self.account_type = input('enter the account type ')
        self.amount = int(input('enter your first deposit '))
        self.autogenerate_account_number()

    def create_transaction(self,transaction):
        self.transaction_history[datetime.datetime.now()]=transaction

    def update_amount(self,amount):
        self.amount+=amount
        print('amount update to your account')

    def display_amount(self):
        pass

    def display_transactions(self):
        pass
