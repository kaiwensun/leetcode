class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        @cache
        def dp(i, k):
            if k == 0:
                return 0
            if k < 0:
                return float("-inf")
            if i == len(piles):
                return float("-inf")
            res = dp(i + 1, k)
            sm = 0
            for j in range(min(k, len(piles[i]))):
                sm += piles[i][j]
                res = max(res, sm + dp(i + 1, k - j - 1))
            return res
        return dp(0, k)

