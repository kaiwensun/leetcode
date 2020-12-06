class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i, j = 0, len(nums) - 1
        res = 0
        while i < j:
            if nums[i] + nums[j] == k:
                i += 1
                j -= 1
                res += 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        return res

