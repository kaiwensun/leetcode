import collections
class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        mx = 0
        counter = collections.Counter()
        existence = collections.Counter()
        res = 0
        for i, n in enumerate(nums):
            existence[counter[n]] -= 1
            counter[n] += 1
            existence[counter[n]] += 1
            mx = max(mx, counter[n])
            if existence[mx] == 1 and existence[mx - 1] == -existence[0] - 1:
                res = i
            elif existence[1] == 1 and existence[mx] == -existence[0] - 1:
                res = i
            elif mx == 1:
                res = i
        return res + 1
            
