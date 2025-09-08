class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return int(any(num != nums[0] for num in nums))

