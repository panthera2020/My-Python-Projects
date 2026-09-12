from unittest import TestCase

from check_out import CheckOut

class TestCheckOut(TestCase):
    def setUp(self):
        self.check_out = CheckOut()

    def test_thatCashierCan_addOneItem(self):
        self.check_out.addItem('Parfait',2,2100)
        self.assertEqual(1, len(self.check_out.get_item()))

    def test_thatCashierCan_addTwoItems(self):
        self.check_out.addItem('Parfait',2,2100)
        self.check_out.addItem('Biscuit',3,2200)
        self.assertEqual(2, len(self.check_out.get_item()))

    def test_thatWhenCashierAddItems_IGetSubtotalOfItems(self):
        self.check_out.addItem('Parfait',2,2000)
        self.check_out.addItem('Biscuit',4,1000)
        self.assertEqual(8000, self.check_out.get_subtotal())

    def test_thatWhenCashierAddItems_IGetAmountOfDiscount(self):
        self.check_out.addItem('Parfait',2,2000)
        self.check_out.addItem('Biscuit',4,1000)
        self.assertEqual(800, self.check_out.get_discount(10))

    def test_thatWhenIAddItems_iGetVatOfTotalOrder(self):
        self.check_out.addItem('Parfait',2,2000)
        self.check_out.addItem('Biscuit',4,1000)
        self.assertEqual(600, self.check_out.get_vat())

    def test_thatWhenIAddItems_IGetTotalBill(self):
        self.check_out.addItem('Parfait',2,2000)
        self.check_out.addItem('Biscuit',4,1000)
        self.assertEqual(7800, self.check_out.get_total_bill(10))

    def test_thatWhenIAddItems_AndIGetAmountFromCustomer_IGetChangeToReturn(self):
        self.check_out.addItem('Parfait',2,2000)
        self.check_out.addItem('Biscuit',4,1000)
        self.assertEqual(200, self.check_out.get_change(8000,10))