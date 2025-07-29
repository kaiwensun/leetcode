class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return sum(nums[i] for i in range(n // 3, n, 2))

