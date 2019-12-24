### THis solution TLE

import functools
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        @functools.lru_cache(None)
        def isComprised(word):
            if word in words_set:
                return True
            for length in lengths:
                if length >= len(word):
                    break
                if word[:length] in words_set and isComprised(word[length:]):
                    return True
            return False

        words = list(filter(len, words))
        lengths = sorted(map(len, words))
        words_set = set(words)
        res = []
        for word in words:
            for length in lengths:
                if length >= len(word):
                    break
                if word[:length] in words_set and isComprised(word[length:]):
                    res.append(word)
                    break
        return res
