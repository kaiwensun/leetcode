import bisect

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        split = bisect.bisect_right(nums, (target - 1) // 2)
        res = split * (split - 1) // 2
        l = split - 1
        for r in range(split, len(nums)):
            while l >= 0 and nums[l] + nums[r] >= target:
                l -= 1
            res += l + 1
        return res

