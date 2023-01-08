import bisect

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(bisect.bisect_left(nums, 0), len(nums) - bisect.bisect_right(nums, 0))

