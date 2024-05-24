class CashManager:
    def __init__(self):
        self.current_cash = 0
        self.input_cash = 0

    def add_coin(self):
        self.input_cash += int(input('enter the number of coins you want to add'))
        print(f'You have added {self.input_cash}')

    def return_money(self, money):
        self.input_cash -= money
        print(f'Money Returned:{money}')

    def add_to_total(self):
        self.current_cash += self.input_cash
        self.input_cash = 0

