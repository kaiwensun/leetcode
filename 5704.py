class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = j = k
        mn = res = nums[k]
        while i >= 0 or j < len(nums):
            while i >= 0 and nums[i] >= mn:
                i -= 1
            while j < len(nums) and nums[j] >= mn:
                j += 1
            res = max(res, mn * (j - i - 1))
            mn = max(float("-inf") if i < 0 else nums[i], float("-inf") if j >= len(nums) else nums[j])
        return res

