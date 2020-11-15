from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        return set(word1) == set(word2) and sorted(cnt1.values()) == sorted(cnt2.values())

