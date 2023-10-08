from functools import cache

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diff = [index for index, is_diff in enumerate(c1 != c2 for c1, c2 in zip(s1, s2)) if is_diff]
        if len(diff) % 2:
            return -1
        if not diff:
            return 0
        res = 0

        def pair(i, j):
            if j >= len(diff):
                return float("inf")
            return min(x, diff[j] - diff[i])

        @cache
        def dp(i, unpaired_i):
            if i == len(diff):
                return 0 if unpaired_i is None else float("inf")
            if i > len(diff):
                return float("inf")
            res = pair(i, i + 1) + dp(i + 2, unpaired_i)
            if unpaired_i is not None:
                res = min(res, pair(unpaired_i, i) + dp(i + 1, None))
            else:
                res = min(res, dp(i + 1, i))
            return res

        return dp(0, None)

