import string

class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set('aeiouAEIOU')
        consonants = set(string.ascii_letters) - vowels
        symbols = set("@#$")
        word_set = set(word)
        return bool(len(word) >= 3 and word_set & vowels and word_set & consonants and not (word_set & symbols))

