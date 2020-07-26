import collections
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter()
        res = 0
        for num in nums:
            res += cnt[num]
            cnt[num] += 1
        return res
