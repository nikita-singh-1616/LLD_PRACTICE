

from classes.account import Bank1Account
from classes.user import BankUser
from intefaces.bank_interface import BankInterface


class Bank1(BankInterface):
    def __init__(self):
        self.current_user = None
        self.accounts = {} # {account_no:account}
        self.card_accounts = {}
        if not self.current_user:
            self.welcome()
        else:
            self.menu()

    def menu(self):
        print('TBD')

    def welcome(self):
        while True:
            inp = int(input('Press 1 to login\nPress 2 to use the create an account\nPress 3 to exit'))
            if inp == 1:
                self.login()
            elif inp == 2:
                self.create_account()
            elif inp == 3:
                return 
        
    def search_account_from_account_number(self,account_no):
        pass

    def search_account_from_card_number(self,card_no):
        pass

    def create_account(self):
        print('creating an account')
        user = BankUser()
        user.create_user()
        print('user registered')
        account = Bank1Account()
        account.create_account(user)
        self.accounts[account.account_number]=account
        print('account created successfully!')


    def create_card(self):
        pass

    def login(self):
        email = input('enter your registered email ID ')
        # check for emails in registered users
        user = None
        for i in self.accounts.values():
            if i.user.get_user_specific_details('email') == email:
                user = i.user
                break
        if not user:
            print('Invalid Email.')
            return False
        while True:
            password = input('enter your password ')
            if user.validate_login(email,password):
                self.current_user = user
                print('Login successful.')
                break
            else:
                print('Wrong Password ')
