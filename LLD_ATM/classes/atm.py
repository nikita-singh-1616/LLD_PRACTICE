from classes.transaction1 import Transaction1
from static import Constants
from intefaces.atm_interface import ATMInterface


class ATM(ATMInterface):
    def __init__(self,bank):
        super().__init__()
        self.banks = bank
        
    def start(self):
        while True:
            self.enter_card_no()

    def enter_card_no(self):
        card_no = input(f'enter your card number, enter exit to exit the atm.\n')
        account,card = self.bank.check_if_card_exists(card_no)
        if not account:
            print('invalid card number')
            return 
        pin = input(int(f'enter the pin no.\n'))
        if card.validate_pin(pin):
            self.current_account = account
            inp = int(input('Press1 to view your account details\nPress2 to withdraw amount\nPress 3 to deposit amount\n press 4 to transfer money to other account\n press 5 to exit'))
            if inp == 1:
                print(f'viewing account details')
                self.view_account_details()
            elif inp == 2:
                print(f'withdraw')
                self.withdraw_amount()
            elif inp == 3:
                print(f'deposit')
                self.deposit_amount()
            elif inp == 4:
                print(f'transfer money')
                self.transfer_money()
            elif inp == 5:
                print('Thank You Visit again')
                return 
        else:
            print('Incorrect Pin')
            return 
    def view_account_details(self):
        self.current_account.show_account_details()

    def withdraw_amount(self):
        transaction = Transaction1()
        try:
            amount = int(input('enter the amount'))
            self.current_account.update_amount(amount*(-1))
            transaction.create_transaction(Constants.transaction_types.get('withdraw'),amount*(-1),self.current_account.send_specific_data('account_no'),None)
            self.current_account.create_transaction(transaction)
            print(f'money withdrawn successfully\n')
        except ValueError as e:
            print(str(e))

    def deposit_amount(self):
        transaction = Transaction1()
        try:
            amount = int(input('enter the amount'))
            self.current_account.update_amount(amount)
            transaction.create_transaction(Constants.transaction_types.get('deposit'),amount,None,self.current_account.send_specific_data('account_no'))
            self.current_account.create_transaction(transaction)
            print(f'money deposited successfully\n')
        except ValueError as e:
            print(str(e))

    def transfer_money(self):
        transfer_to = input("enter the reciever's account number: ")
        amount = int(input("enter the amount to be transferred"))
        current_account_no = self.current_account.send_specific_data('account_no')
        if transfer_to not in self.bank.accounts:
            print(f'invalid account number\n')
        elif transfer_to == current_account_no:
            print(f'cannot transfer to current account\n')
        else:
            self.current_account.update_amount(amount*(-1))
            transaction = Transaction1()
            transaction.create_transaction(Constants.transaction_types.get('transfer'),-amount,current_account_no,transfer_to)
            self.current_account.create_transaction(transaction)
            self.accounts[transfer_to].update_amount(amount)
            transaction2 = Transaction1()
            transaction2.create_transaction(Constants.transaction_types.get('transfer'),amount,current_account_no,transfer_to)
            self.accounts[transfer_to].create_transaction(transaction2)
            print(f'Money transferred from {current_account_no} to {transfer_to}\n')

            
        
        
    
