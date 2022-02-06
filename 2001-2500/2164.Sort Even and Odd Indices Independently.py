class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rearraged = [sorted(nums[::2]), sorted(nums[1::2], reverse=True)]
        return [rearraged[i % 2][i // 2] for i in range(len(nums))]

