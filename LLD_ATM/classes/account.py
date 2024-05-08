import datetime
from classes.card import Card
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
        if self.amount+amount<0:
            raise ValueError('Invalid withdrawal amount')

        self.amount+=amount
        print('amount update to your account')

    def show_account_details(self):
        user_name = self.user.get_user_specific_details('name')
        phone = self.user.get_user_specific_details('phone')
        email = self.user.get_user_specific_details('email')
        date_of_birth = self.user.get_user_specific_details('date_of_birth')
        print(f'\n\tUSER DETAILS\nUsername: {user_name}\nPhone:{phone}\nWmail:{email}\nDOB:{date_of_birth}\n\tACCOUNT DETAILS\n'
        f'Account Number:{self.account_number}\nAccount Balance:{self.amount}\nAccountType:{self.account_type}')
        self.display_transactions()

    def display_transactions(self):
        if self.transaction_history.values():
            print('\n\tTRANSACTION HISTORY\n')
            print('Txn Type\tAmount\tTxn Date\t\tFrom\tTo')
            for i in self.transaction_history.values():
                i.display_transaction()
        else:
            print('No Transactions To Display')

    def send_specific_data(self,data):
        data_dict = {
            'account_no':self.account_number,
            'user':self.user,
            'amount':self.amount, 
            'type':self.account_type,
            'transacations':self.transaction_history
        }
        if data not in data_dict:
            return False
        return data_dict[data]

    def create_debit_card(self,bank):
        card = Card()
        card.create_card(bank)
        card.set_pin()


