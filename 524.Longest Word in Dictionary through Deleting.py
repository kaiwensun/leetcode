from collections import Counter
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        s_set = set(s)
        d = sorted(
            (word for word in set(d) if set(word) <= s_set and len(word) <= len(s)),
            key=lambda word: (-len(word), word))
        s_counter = Counter(s)
        for word in d:
            if self.is_sub_sequence(s, word):
                return word
        return ''
    def is_sub_sequence(self, s, word):
        i = j = 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                j += 1
            i += 1
        return j == len(word)
