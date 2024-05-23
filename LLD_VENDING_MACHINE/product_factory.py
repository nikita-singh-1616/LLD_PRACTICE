from abc import ABC, abstractmethod


class ProductAbstractClass(ABC):
    def __init__(self):
        self.id = None
        self.code = None
        # self.price = None


class Product(ProductAbstractClass):
    def __init__(self, id, code):
        super().__init__()
        self.id = id
        self.code = code
        # self.price = 10


class ProductShelf:
    def __init__(self, code, price, products):
        self.code = code
        self.products = products
        self.count = len(products)
        self.price = price

    def purchase_product(self):
        if self.products:
            product = self.products.pop()
            self.count -= 1
            return product
        else:
            return None

    def display_shelf(self):
        print(f'{self.code}\t{self.price}\t{self.count}')


class ProductShelfManager:
    def __init__(self):
        self.factory = {}

    def add_to_factory(self, code, shelf):
        self.factory[code] = shelf

    def get_shelf(self, code):
        if code in self.factory:
            return self.factory[code]
        return None
