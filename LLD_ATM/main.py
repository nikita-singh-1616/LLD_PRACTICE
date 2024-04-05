from classes.bank1 import Bank1


class Main:
    def __init__(self) -> None:
        self.welcome()

    def welcome(self):
        print('ok')
        while True:
            inp = int(input('Press 1 to check into bank\nPress 2 to use the atm\nPress 3 to exit main\n\n'))
            if inp == 1:
                Bank1()
            elif inp == 2:
                print('atm functionality')
            elif inp == 3:
                print('thank you, visit again')
                break

start = Main()