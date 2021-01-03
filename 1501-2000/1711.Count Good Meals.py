from collections import Counter
class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        seen = Counter()
        res = 0
        for item in deliciousness:
            for shift in xrange(22):
                res += seen.get((1 << shift) - item, 0)
            seen[item] += 1
        return res % (10 ** 9 + 7)

