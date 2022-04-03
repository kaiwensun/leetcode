class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        N = len(nums)
        up = 1
        for i in range(2, N):
            up *= i
        res = 0
        down = up
        for i in range(N - 1):
            res += (nums[i] * up // down) % 10
            up //= i + 1
            down //= N - 1 - i
        res += (nums[-1] * up // down) % 10
        return res % 10

