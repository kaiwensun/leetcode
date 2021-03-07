from collections import Counter

class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in xrange(len(s)):
            counter = Counter()
            for j in xrange(i, len(s)):
                counter[s[j]] += 1
                res += max(counter.values()) - min(counter.values())
        return res

