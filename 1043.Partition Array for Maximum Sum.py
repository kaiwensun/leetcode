import functools
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        @functools.lru_cache(None)
        def helper(i, j):
            # The helper finds the max result of the range [i, j)
            if j - i <= K:
                return (j - i) * max(A[i:j])
            return max(helper(i, newj) + helper(newj, j) for newj in range(i + 1, i + 1 + K))
        
        return helper(0, len(A))
