import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        if ones:
            return len(nums) - ones
        steps = 0
        N = len(nums)
        while nums:
            steps += 1
            nums = [math.gcd(nums[i], nums[i + 1]) for i in range(len(nums) - 1)]
            if 1 in nums:
                return steps + N - 1
        return -1

