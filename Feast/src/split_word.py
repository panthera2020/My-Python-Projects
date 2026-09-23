
class split_word:
    def split_word_left(self, word, character):
        for index, letter in enumerate(word):
            if letter == character: return word[index - len(word):: -1]

    def splt_word_right(self, word, character):
        for index, letter in enumerate(word):
            if letter == character: return word[:index - len(word) -1: -1]

    def splt_word_round(self, word, character):
        if character in word: return self.split_word_left(word, character) + self.splt_word_right(word, character)
        else: return word
