import functools
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        num2index = {num: index for index, num in enumerate(A)}
        @functools.lru_cache(None)
        def dp(a, b):
            c = a + b
            if c not in num2index:
                return 0
            return 1 + dp(b, c)
        res = max(dp(A[i], A[j]) for i in range(len(A)) for j in range(i + 1, len(A)))
        return 0 if res == 0 else res + 2
