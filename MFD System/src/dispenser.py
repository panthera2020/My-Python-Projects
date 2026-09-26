# from Product import Product

class Dispenser:
    def __init__(self):
        self.products = []

    def add_product(self, Product):
        self.products.append(Product)

    def get_last_product(self):
        return self.products[-1]

    def get_products(self):
        return self.products
