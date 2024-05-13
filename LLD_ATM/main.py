from classes.atm import ATM
from classes.bank1 import Bank1


class Main:
    def __init__(self) -> None:
        self.bank = Bank1()
        self.atm = ATM(self.bank)
        self.welcome()

    def welcome(self):
        while True:
            inp = int(input('Press 1 to check into bank\nPress 2 to use the atm\nPress 3 to exit main\n\n'))
            if inp == 1:
                self.bank.login_user_menu()
            elif inp == 2:
                self.atm.start()
            elif inp == 3:
                print('thank you, visit again')
                break

start = Main()