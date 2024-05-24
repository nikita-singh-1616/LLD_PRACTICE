from LLD_VENDING_MACHINE.states.product_selection_state import ProductSelectionState
from LLD_VENDING_MACHINE.states.state_manager import State


class HasCoinState(State):
    def __init__(self,machine):
        super().__init__()
        self.vending_machine = machine

    def display(self):
        inp = int(input(f'Press 1 to insert coin\nPress 2 to start product selection \nPress 3 to cancel\nPress 4 to view the vending machine\n'))
        hash_ = {
            1:self.insert_coin,
            2:self.select_product,
            3:self.cancel,
            4:self.display_vending_machine
        }
        return hash_[inp]()

    def insert_coin(self):
        print('insert coins')
        self.vending_machine.cash_manager.add_coin()

    def select_product(self):
        print('select product ')
        self.vending_machine.state = ProductSelectionState(self.vending_machine)

    def cancel(self):
        print('cancel')
        money_to_return = self.vending_machine.cash_manager.input_cash
        self.vending_machine.cash_manager.return_money(money_to_return)

    def press_insert_coin(self):
        print(self.default_msg)

    def use_keypad(self):
        print(self.default_msg)
        pass

    def checkout(self):
        print(self.default_msg)

    def dispense_product(self):
        print(self.default_msg)
        pass

    def display_vending_machine(self):
        self.vending_machine.product_manager.display_products()
