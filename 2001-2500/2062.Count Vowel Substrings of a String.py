class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        res = 0
        for start in range(len(word)):
            for end in range(start + 1, len(word) + 1):
                if set(word[start:end]) == set("aeiou"):
                    res += 1
        return res

