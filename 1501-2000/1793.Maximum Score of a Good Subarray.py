class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = j = k
        n = len(nums)
        nums.append(float("-inf"))
        mn = res = nums[k]
        while i >= 0 or j < n:
            while i >= 0 and nums[i] >= mn:
                i -= 1
            while j < n and nums[j] >= mn:
                j += 1
            res = max(res, mn * (j - i - 1))
            mn = max(nums[i], nums[j])
        return res

