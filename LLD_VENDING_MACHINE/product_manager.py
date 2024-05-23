from LLD_VENDING_MACHINE.product_factory import ProductShelfManager, Product, ProductShelf


class ProductManager:
    def __init__(self):
        self.product_shelf_manager = ProductShelfManager()
        self.product_codes = [{
            'code': '1apple',
            'price': 10
        },
        {
            'code': '2banana',
            'price': 20
        },
        {
            'code': '3orange',
            'price': 30
        }]
        self.product_count = 20
        self.create_shelves()

    def create_shelves(self):
        for i in self.product_codes:
            product_code = i['code']
            price = i['price']
            product = []
            for count in range(self.product_count):
                product.append(Product(count + 1, product_code))
            product_shelf = ProductShelf(product_code, price, product)
            self.product_shelf_manager.add_to_factory(product_code, product_shelf)
        print('product shelves are created.')

    def display_products(self):
        print('Vending Machine')
        print('Product Code\tPrice\tQty.')
        for i in self.product_codes:
            shelf = self.product_shelf_manager.get_shelf(i['code'])
            shelf.display_shelf()
        print('\n')

    def validate_details(self, code, amount):
        shelf = self.product_shelf_manager.get_shelf(code)
        if shelf.price == amount:
            product = shelf.purchase_product()
            if product:
                return product
            else:
                print('Item is out of stock.Initiating refund')
#                 initiate refund
