
import itertools

def anagram(word):
    return ["".join(p) for p in itertools.permutations(word)]

print(anagram("abc"))

word = 'abc'

for p in itertools.permutations(word):
    print(p)
