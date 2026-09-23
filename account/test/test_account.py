import unittest

from Account import Account

class MyTestCase(unittest.TestCase):
    def test_that_account_can_be_created(self):
        account = Account("Bob")
        self.assertEqual(account.balance, 0)
        self.assertEqual(account.name, "bob")

    def test_that_account_can_receive_deposit(self):
        account = Account("Bob")
        account.deposit(1000)
        self.assertEqual(account.balance, 1000)

    def test_that_account_cannot_recieve_negative_deposit(self):
        account = Account("Bob")
        self.assertRaises(ValueError, account.deposit, -1000)

    def test_that_you_can_withdraw_from_account_after_deposit(self):
        account = Account("Bob")
        account.deposit(1000)
        account.withdraw(500)
        self.assertEqual(account.balance, 500)

    def test_that_you_cannot_withdraw_more_than_balance(self):
        account = Account("Bob")
        account.deposit(1000)
        account.withdraw(2000)
        self.assertEqual(account.balance, 1000)

    def test_that_you_cannot_withdraw_when_balance_is_zero(self):
        account = Account("Bob")
        account.withdraw(1000)
        self.assertEqual(account.balance, 0)

    def test_that_you_cannot_withdraw_negative(self):
        account = Account("Bob")
        self.assertRaises(ValueError, account.withdraw, -1000)

if __name__ == '__main__':
    unittest.main()
