from collections import Counter
class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        return sum(x & 1 for x in Counter(s).values()) <= k <= len(s)
