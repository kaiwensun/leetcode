import functools
class Solution(object):
    
    def minScoreTriangulation(self, A):
        self.A = A
        return self.helper(0, len(A) - 1)
        
    @functools.lru_cache(None)
    def helper(self, i, j):
        A = self.A
        if j - i == 2:
            return A[i] * A[i + 1] * A[i + 2]
        if j - i < 2:
            return 0
        res = float('inf')
        for k in range(i + 1, j):
            res = min(res, self.helper(i, k) + self.helper(k, j) + A[i] * A[k] * A[j])
        return res
