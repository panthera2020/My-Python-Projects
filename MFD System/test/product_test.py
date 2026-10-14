import unittest
from product import Product
from product_type import ProductType


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

    def test_that_a_new_product_starts_with_zero_amount_zero_liters_and_no_date(self):
        self.assertEqual(0, self.product.get_amount())
        self.assertEqual(0, self.product.get_liter())
        self.assertEqual("", self.product.get_date())

    def test_that_i_can_set_the_amount_directly(self):
        self.product.set_amount(500)
        self.assertEqual(500, self.product.get_amount())

    def test_that_every_product_type_gets_its_own_name_and_price(self):
        expected = {1: ("PETROL", 650), 2: ("DIESEL", 720), 3: ("KEROSENE", 550), 4: ("GAS", 480)}
        for number, (name, price) in expected.items():
            with self.subTest(number=number):
                product = Product()
                product.set_product_type(number)
                self.assertEqual(name, product.get_product_name())
                self.assertEqual(price, product.get_product_type().value)

    def test_that_amount_is_worked_out_from_liters_for_every_product_type(self):
        for number, price in {1: 650, 2: 720, 3: 550, 4: 480}.items():
            with self.subTest(number=number):
                product = Product()
                product.set_product_type(number)
                product.set_amount_of(3)
                self.assertEqual(3 * price, product.get_amount())
                self.assertEqual(3, product.get_liter())

    def test_that_liters_are_worked_out_from_amount_for_every_product_type(self):
        for number, price in {1: 650, 2: 720, 3: 550, 4: 480}.items():
            with self.subTest(number=number):
                product = Product()
                product.set_product_type(number)
                product.set_liter_of(price * 4)
                self.assertEqual(4, product.get_liter())
                self.assertEqual(price * 4, product.get_amount())

    def test_that_an_amount_that_does_not_divide_evenly_gives_fractional_liters(self):
        self.product.set_product_type(1)
        self.product.set_liter_of(1000)
        self.assertAlmostEqual(1000 / 650, self.product.get_liter())

    def test_that_fractional_liters_give_the_right_amount(self):
        self.product.set_product_type(2)
        self.product.set_amount_of(2.5)
        self.assertEqual(1800, self.product.get_amount())

    def test_that_amount_to_liters_and_back_returns_the_same_amount(self):
        self.product.set_product_type(3)
        self.product.set_liter_of(1100)
        liters = self.product.get_liter()
        self.product.set_amount_of(liters)
        self.assertEqual(1100, self.product.get_amount())

    def test_that_changing_the_product_type_changes_the_price_used(self):
        self.product.set_product_type(1)
        self.product.set_amount_of(2)
        self.assertEqual(1300, self.product.get_amount())
        self.product.set_product_type(4)
        self.product.set_amount_of(2)
        self.assertEqual(960, self.product.get_amount())

    def test_that_an_unknown_number_does_not_change_the_product_type(self):
        self.product.set_product_type(2)
        for number in [0, 5, -1, 99]:
            with self.subTest(number=number):
                self.product.set_product_type(number)
                self.assertEqual(ProductType.DIESEL, self.product.get_product_type())

    def test_that_an_unknown_number_does_not_set_a_date(self):
        self.product.set_product_type(7)
        self.assertEqual("", self.product.get_date())

    def test_that_a_text_number_is_not_accepted_as_a_product_type(self):
        self.product.set_product_type("1")
        self.assertNotEqual(ProductType.PETROL, self.product.get_product_type())