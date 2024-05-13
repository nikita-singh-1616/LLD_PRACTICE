import datetime
import random
from intefaces.card_interface import CardInterface


class Card(CardInterface):
    def __init__(self) -> None:
        super().__init__()

    def create_card(self,bank):
        print('card')
        self.card_no = self.create_card_number()
        self.bank = bank
        self.expiry_date = datetime.datetime.now()+datetime.timedelta(5)
        print('Your debit card is now created but inactive, it will be active after 2 mins.')
        return self.card_no

    def create_card_number(self):
        print('rand')
        return random.randint(1000000,9999999)

    def activate_card(self):
        self.status = True
        print(f'Your card with cardnumber {self.card_no} is now active.\n')
    
    def check_status(self):
        print(self.status)
    
    def validate_pin(self,pin):
        if self.pin == pin:
            print('PIN MATCHED')
            return True
        else:
            print('INVALID PIN')
            return False

    def set_pin(self):
        pin = input('enter your pin number ')
        self.pin = pin
        print('Your debit card pin has been set.')

    def validate_card(self):
        pass
    
        
