import string

class PasswordEncryption:
    def __init__(self,  password = str):
        self.password = password
        self.characters = string.ascii_letters

    def find_index(self,character):
        index = 0
        for letter in self.characters:
            if letter == character:
                return index
            index += 1
        return -1

    def encrypt(self):
        encrypted_password = ''
        for letter in self.password:
            index = self.find_index(letter)
            if index != -1:
                if index > 37:
                    sum = len(self.characters) - index
                    index = 13 - sum
                else: index = index  + 13

                character = self.characters[index]
                if letter.isupper():
                    encrypted_password += character.upper()
                elif letter.islower():
                    encrypted_password += character.lower()

            else: encrypted_password += letter
        return encrypted_password

    def decrypt(self):
        decrypted_password = ''
        encrypted_password = self.encrypt()
        for letter in encrypted_password:
            index = self.find_index(letter)
            if index != -1:
                if index < 13: index = (len(self.characters) - 1) - (12 - index)
                else: index = index -13

                character = self.characters[index]
                if letter.isupper():
                    decrypted_password += character.upper()
                elif letter.islower():
                    decrypted_password += character.lower()

            else: decrypted_password += letter
        return decrypted_password



