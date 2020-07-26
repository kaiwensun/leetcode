import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        if k == 0:
            return sum(v > 1 for v in collections.Counter(nums).values())
        nums = set(nums)
        return sum(num + k in nums for num in nums)
