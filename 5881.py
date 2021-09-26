class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = float("-inf")
        mn = float("inf")
        for num in nums:
            res = max(res, num - mn)
            mn = min(mn, num)
        return -1 if res <= 0 else res

