from collections import Counter
class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter()
        res = 0
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                cnt[nums[i] * nums[j]] += 1
        for value in cnt.values():
            res += value * (value - 1)
        return res * 4

