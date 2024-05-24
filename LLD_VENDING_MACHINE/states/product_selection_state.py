from LLD_VENDING_MACHINE.states.checkout_state import Checkout
from LLD_VENDING_MACHINE.states.state_manager import State


class ProductSelectionState(State):
    def __init__(self, machine):
        super().__init__()
        self.vending_machine = machine

    def display(self):
        inp = int(input(f'Press 1 to activate keypad\nPress 2 to checkout \nPress 3 to cancel\nPress 4 to view the vending machine\n'))
        hash_ = {
            1: self.use_keypad,
            2: self.checkout,
            3: self.cancel,
            4: self.display_vending_machine
        }
        return hash_[inp]()

    def use_keypad(self):
        print('keypad active')
        product_code = input('enter the product code: ')
        input_cash = self.vending_machine.cash_manager.input_cash
        if self.vending_machine.product_manager.validate_details(product_code,input_cash):
            inp = int(input('You have inserted sufficient amount. \nPress 1 to checkout\nPress 2 to go back'))
            if inp == 1:
                self.checkout(product_code)
            elif inp == 2:
                self.use_keypad()
    def checkout(self,product_code):
        self.vending_machine.state = Checkout(self.vending_machine,product_code)

    def cancel(self):
        money_to_return = self.vending_machine.cash_manager.input_cash
        self.vending_machine.cash_manager.return_money(money_to_return)
        self.vending_machine.state = None

    def insert_coin(self):
        print(self.default_msg)
        pass

    def press_insert_coin(self):
        print(self.default_msg)
        pass

    def select_product(self):
        print(self.default_msg)
        pass

    def dispense_product(self):
        print(self.default_msg)
        pass

    def display_vending_machine(self):
        self.vending_machine.product_manager.display_products()
        pass
