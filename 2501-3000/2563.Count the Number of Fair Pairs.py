import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        nums.sort()
        for i, num in enumerate(nums):
            l = bisect.bisect_left(nums, lower - num)
            r = bisect.bisect_right(nums, upper - num)
            res += r - l
            print(i, num, res, r, l)
            if l <= i < r:
                res -= 1
        return res // 2

