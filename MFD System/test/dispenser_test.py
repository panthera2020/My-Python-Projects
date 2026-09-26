import unittest

from Product import Product
from dispenser import Dispenser

class DispenserTest(unittest.TestCase):

    def test_that_product_bought_is_added(self):
        dispenser = Dispenser()
        product = Product()
        dispenser.add_product(product)
        self.assertEqual(len(dispenser.products), 1)

    def test_that_that_i_get_last_product_added(self):
        dispenser = Dispenser()
        product = Product()
        dispenser.add_product(product)
        last_product = dispenser.get_last_product()
        self.assertEqual(0, last_product.get_amount())
        self.assertEqual(0,last_product.get_liter())

    def test_that_when_i_add_various_products_i_get_all_products_added(self):
        dispenser = Dispenser()
        product = Product()
        product_two = Product()
        product_three = Product()
        dispenser.add_product(product)
        dispenser.add_product(product_two)
        dispenser.add_product(product_three)
        products = dispenser.get_products()
        self.assertEqual(len(products), 3)