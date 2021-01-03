class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        mid_end_min = mid_end_max = 0
        left = mid_min = mid_max = 0
        right = sum(nums)
        for left_end in xrange(len(nums) - 2):
            left += nums[left_end]
            mid_min -= nums[left_end]
            mid_max -= nums[left_end]
            while mid_end_min <= left_end + 1 or (mid_min < left and mid_end_min < len(nums)):
                mid_min += nums[mid_end_min]
                mid_end_min += 1
            while mid_end_max < len(nums) - 1 and mid_max + nums[mid_end_max] <= right - nums[mid_end_max]:
                mid_max += nums[mid_end_max]
                right -= nums[mid_end_max]
                mid_end_max += 1
            res += max(0, mid_end_max - mid_end_min + 1)
        return res % (10 ** 9 + 7)


