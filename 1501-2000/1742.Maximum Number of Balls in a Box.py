from collections import Counter
class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        cnt = Counter()
        for i in xrange(lowLimit, highLimit + 1):
            key = 0
            while i != 0:
                key += i % 10
                i /= 10
            cnt[key] += 1
        return max(cnt.values())

