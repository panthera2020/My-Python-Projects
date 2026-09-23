
class palindrome:
    def is_palindrome(self, word):
        new_word = word.lower()
        return new_word == new_word[::-1]

    def is_palindrome_in(self, words):
        return [self.is_palindrome(word) for word in words]