class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        @lru_cache(None)
        def dp(l, r):
            res = 0
            for mid in range(l + 1, r):
                left = 1 if l == -1 else nums[l]
                right = 1 if r == len(nums) else nums[r]
                res = max(res, dp(l, mid) + dp(mid, r) + left * nums[mid] * right)
            return res
        return dp(-1, len(nums))

