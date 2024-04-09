

from classes.transaction1 import Transaction1
from static import Constants
from classes.account import Bank1Account
from classes.user import BankUser
from intefaces.bank_interface import BankInterface


class Bank1(BankInterface):
    def __init__(self):
        self.current_user = None
        self.current_account = None
        self.accounts = {} # {account_no:account}
        self.card_accounts = {}
        self.login_user_menu()

    def login_user_menu(self):
        while True:
            if self.current_user:
                inp = int(input('Press1 to view your account details\nPress2 to withdraw amount\nPress 3 to deposit amount\n press 4 to transfer money to other account\n press 5 to request a debit card\npress6 to exit'))
                if inp == 1:
                    print('viewing account details')
                    self.view_account_details()
                elif inp == 2:
                    print('withdraw')
                    self.withdraw_amount()
                elif inp == 3:
                    print('deposit')
                    self.deposit_amount()
                elif inp == 4:
                    print('transfer money')
                elif inp == 5:
                    print('request a card')
                elif inp == 6:
                    return
            else:
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
        print('Account created successfully,please login again to continue or exit')


    def create_card(self):
        pass

    def login(self):
        email = input('enter your registered email ID ')
        # check for emails in registered users
        user = None
        for i in self.accounts.values():
            if i.user.get_user_specific_details('email') == email:
                user = i.user
                self.current_account = i
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

    def view_account_details(self):
        self.current_account.show_account_details()

    def withdraw_amount(self):
        transaction = Transaction1()
        try:
            amount = int(input('enter the amount'))
            self.current_account.update_amount(amount*(-1))
            transaction.create_transaction(Constants.transaction_types.get('withdraw'),amount*(-1))
            self.current_account.create_transaction(transaction)
        except ValueError as e:
            print(str(e))

    def deposit_amount(self):
        transaction = Transaction1()
        try:
            amount = int(input('enter the amount'))
            self.current_account.update_amount(amount)
            transaction.create_transaction(Constants.transaction_types.get('deposit'),amount)
            self.current_account.create_transaction(transaction)
        except ValueError as e:
            print(str(e))

    def transfer_money(self):
        transfer_to = input("enter the reciever's account number: ")
        amount = input("enter the amount to be transferred")
        if transfer_to not in self.accounts:
            print('invalid account number')
        elif transfer_to == self.current_account.send_specific_data('account_no'):
            print('cannot transfer to current account')
        else:
            self.current_account.update_amount(amount*(-1))
            self.accounts[transfer_to].update_amount(amount)


