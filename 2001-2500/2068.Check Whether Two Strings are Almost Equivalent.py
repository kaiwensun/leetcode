from collections import Counter

class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return all(map(lambda c: abs(cnt1[c] - cnt2[c]) <= 3, set(cnt1.keys()) | set(cnt2.keys())))

