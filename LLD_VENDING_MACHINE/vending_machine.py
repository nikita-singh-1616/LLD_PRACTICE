from LLD_VENDING_MACHINE.product_manager import ProductManager
from LLD_VENDING_MACHINE.states.idle_state import IdleState


class VendingMachine:
    def __init__(self):
        self.state = IdleState(self)
        self.cash_manager = None
        self.product_manager = ProductManager()
        self.product_manager.display_products()
        self.start()

    def start(self):
        while True:
            self.state.display()

VendingMachine()