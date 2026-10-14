import unittest

from password_encryption import PasswordEncryption


class MyTestCase(unittest.TestCase):
    def test_thatWhenIEncrypt_passWordIsEncrypted(self):
        password_encryption = PasswordEncryption("Hello, World!")
        self.assertEqual('Uryyb, Jbeyq!', password_encryption.encrypt())

    def test_thatWhenIEncrypt_andDecrypt_passwordIsDecrypted(self):
        password_encryption = PasswordEncryption("Hello, World!")
        self.assertEqual('Hello, World!', password_encryption.decrypt())


if __name__ == '__main__':
    unittest.main()
