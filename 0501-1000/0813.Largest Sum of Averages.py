import functools
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        # dp[e][k] means among A[:e], having partitioned into k groups, what is the maximum sum?
        acc = [0] * (len(A) + 1)
        for i in range(len(A)):
            acc[i + 1] = acc[i] + A[i]
            
        def mean(i, j):
            if j <= i:
                return 0
            return (acc[j] - acc[i]) / float(j - i)
        
        @functools.lru_cache(None)
        def dp(e, k):
            if e < k or k == 0 or e == 0:
                return 0
            if k == 1:
                return mean(0, e)
            res = 0
            for myGroupStart in range(k - 1, e):
                res = max(res, dp(myGroupStart, k - 1) + mean(myGroupStart, e))
            return res
        return dp(len(A), K)
