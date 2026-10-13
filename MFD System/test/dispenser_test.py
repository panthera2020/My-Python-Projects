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

    def test_that_a_new_dispenser_has_no_products(self):
        self.assertEqual([], Dispenser().get_products())

    def test_that_the_last_product_is_the_one_added_last(self):
        dispenser = Dispenser()
        first = Product()
        second = Product()
        dispenser.add_product(first)
        dispenser.add_product(second)
        self.assertIs(second, dispenser.get_last_product())

    def test_that_products_come_back_in_the_order_they_were_added(self):
        dispenser = Dispenser()
        first, second, third = Product(), Product(), Product()
        for product in (first, second, third):
            dispenser.add_product(product)
        self.assertEqual([first, second, third], dispenser.get_products())

    def test_that_getting_the_last_product_of_an_empty_dispenser_is_an_error(self):
        with self.assertRaises(IndexError):
            Dispenser().get_last_product()

    def test_that_two_dispensers_do_not_share_products(self):
        first_dispenser = Dispenser()
        second_dispenser = Dispenser()
        first_dispenser.add_product(Product())
        self.assertEqual(1, len(first_dispenser.get_products()))
        self.assertEqual(0, len(second_dispenser.get_products()))

    def test_that_the_same_product_added_twice_is_kept_twice(self):
        dispenser = Dispenser()
        product = Product()
        dispenser.add_product(product)
        dispenser.add_product(product)
        self.assertEqual(2, len(dispenser.get_products()))