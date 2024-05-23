from LLD_VENDING_MACHINE.states.has_cash_state import HasCoinState
from LLD_VENDING_MACHINE.states.state_manager import State


class IdleState(State):
    def __init__(self,machine):
        self.vending_machine = machine

    def display(self):
        inp = int(input('Press 1 to start the machine\nPress 2 to view the vending machine\n'))
        if inp == 1:
            self.press_insert_coin()
        elif inp == 2:
            self.display_vending_machine()

    def press_insert_coin(self):
        self.vending_machine.state = HasCoinState(self.vending_machine)

    def insert_coin(self):
        print(self.default_msg)
        pass

    def select_product(self):
        print(self.default_msg)
        pass

    def cancel(self):
        print(self.default_msg)
        pass

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

