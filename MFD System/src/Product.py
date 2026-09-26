from Product_Type import ProductType
from datetime import datetime

class Product:

    def __init__(self):
        self.ProductType = ProductType
        self.amount = 0
        self.liter = 0
        self.date = ""

    def set_amount(self, amount):
        self.amount = amount

    def generate_date(self):
        now = datetime.now()
        self.date = now.strftime("%d/%m/%Y")

    def set_product_type(self, number):
        if number == 1:
            self.ProductType = ProductType.PETROL
            self.generate_date()
        elif number == 2:
            self.ProductType = ProductType.DIESEL
            self.generate_date()
        elif number == 3:
            self.ProductType = ProductType.KEROSENE
            self.generate_date()
        elif number == 4:
            self.ProductType = ProductType.GAS
            self.generate_date()


    def get_product_type(self):
        return self.ProductType

    def set_liter_of(self, amount):
        self.amount = amount
        self.liter = amount / self.ProductType.value

    def get_liter(self):
        return self.liter

    def set_amount_of(self, liters):
        self.liter = liters
        self.amount = liters * self.ProductType.value

    def get_amount(self):
        return self.amount

    def get_product_name(self):
        return self.ProductType.name

    def get_date(self):
        return self.date

