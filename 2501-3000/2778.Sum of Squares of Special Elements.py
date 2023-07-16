class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(num * num for i, num in enumerate(nums) if len(nums) % (i + 1) == 0)

