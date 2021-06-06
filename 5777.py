from collections import Counter

class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        res = 0
        nums = sorted(cnt.keys(), reverse=True)
        for i in xrange(len(nums) - 1):
            res += (len(nums) - 1 - i) * cnt[nums[i]]
        return res

