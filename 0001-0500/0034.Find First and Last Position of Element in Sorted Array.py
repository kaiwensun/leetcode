import bisect
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target) - 1
        return [-1, -1] if not nums or nums[r] != target else [l, r]

