class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        cnt = 0
        for a, b in zip(nums, sorted_nums):
            if a == b:
                cnt += 1
            else:
                break
        for a, b in reversed(zip(nums, sorted_nums)):
            if a == b:
                cnt += 1
            else:
                break
        return max(len(nums) - cnt, 0)
