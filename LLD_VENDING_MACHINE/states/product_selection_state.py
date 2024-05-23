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

    def checkout(self):
        print('checkout ')

    def cancel(self):
        print('cancel')

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
