# from LLD_VENDING_MACHINE.states.idle_state import IdleState
from LLD_VENDING_MACHINE.states.state_manager import State


class Checkout(State):
    def __init__(self,machine,code):
        super().__init__()
        self.vending_machine = machine
        self.code = code

    def display(self):
        print('processing checkout')
        self.dispense_product()
        pass

    def press_insert_coin(self):
        print(self.default_msg)
        pass

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
        input_amount = self.vending_machine.cash_manager.input_cash
        product,amount_to_refund = self.vending_machine.product_manager.despence_products(self.code,input_amount)
        if product:
            print(f'product with id {product.id} has been dispensed.')
        if amount_to_refund:
            self.vending_machine.cash_manager.return_money(amount_to_refund)
        self.vending_machine.cash_manager.add_to_total()
        self.vending_machine.state = None

    def display_vending_machine(self):
        self.vending_machine.product_manager.display_products()
