from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self):
        self.default_msg = 'ACTION NOT ALLOWED'
    @abstractmethod
    def insert_coin(self):
        print(self.default_msg)
        pass
    @abstractmethod
    def press_insert_coin(self):
        print(self.default_msg)
        pass
    @abstractmethod
    def select_product(self):
        print(self.default_msg)
        pass

    @abstractmethod
    def cancel(self):
        print(self.default_msg)
        pass

    @abstractmethod
    def use_keypad(self):
        print(self.default_msg)
        pass
    @abstractmethod
    def checkout(self):
        print(self.default_msg)
    @abstractmethod
    def dispense_product(self):
        print(self.default_msg)
        pass
    @abstractmethod
    def display(self):
        print(self.default_msg)
        pass

    @abstractmethod
    def display_vending_machine(self):
        print(self.default_msg)
        pass










