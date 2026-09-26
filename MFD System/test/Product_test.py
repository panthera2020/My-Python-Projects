import unittest
from Product import Product
from Product_Type import ProductType


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product()

    def test_that_when_i_get_number_i_set_product_type(self):
        self.product.set_product_type(1)
        self.assertEqual(ProductType.PETROL, self.product.get_product_type())
        self.product.set_product_type(2)
        self.assertEqual(ProductType.DIESEL, self.product.get_product_type())
        self.product.set_product_type(3)
        self.assertEqual(ProductType.KEROSENE, self.product.get_product_type())
        self.product.set_product_type(4)
        self.assertEqual(ProductType.GAS, self.product.get_product_type())

    def test_that_when_i_set_product_type_and_get_amount_i_get_liters(self):
        self.product.set_product_type(1)
        self.product.set_liter_of(1300)
        self.assertEqual(2, self.product.get_liter())
        # self.assertEqual(1300,get)

    def test_that_when_i_set_product_type_and_i_get_liters_amount_is_set(self):
        self.product.set_product_type(1)
        self.product.set_amount_of(2)
        self.assertEqual(1300, self.product.get_amount())

    def test_that_when_i_set_product_type_i_get_product_name(self):
        self.product.set_product_type(1)
        self.assertEqual("PETROL", self.product.get_product_name())