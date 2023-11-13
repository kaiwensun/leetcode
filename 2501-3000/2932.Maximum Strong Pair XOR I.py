class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                a, b = nums[i], nums[j]
                if abs(a - b) <= min(a, b):
                    res = max(res, a ^ b)
        return res

