class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return len([num for num in nums if num & 1 == 0]) >= 2

