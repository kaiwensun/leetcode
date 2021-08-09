class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        i = 1
        while i + 1 < len(nums):
            start = i
            while i + 1 < len(nums) and nums[i] - nums[i - 1] == nums[i + 1] - nums[i]:
                i += 1
            size = i - start
            res += (size + 1) * size // 2
            i += 1
        return res

