from collections import Counter
from functools import cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        left, right = [None] * N, [None] * N
        last_index = {}
        for i in range(N):
            left[i] = dict(last_index)
            last_index[s[i]] = i
        last_index = {}
        for i in range(N - 1, -1, -1):
            right[i] = dict(last_index)
            last_index[s[i]] = i
        res = 0

        @cache
        def dp(i, j):
            if min(i, j) < 0 or max(i, j) >= len(s):
                return 0
            res = 0
            if i == j:
                adjust = 1
            elif i - 1 == j:
                adjust = 0
            else:
                adjust = 2
            for c in left[i].keys():
                if c in right[j]:
                    res = max(res, dp(left[i][c], right[j][c]))
            return res + adjust
        return max(max(dp(i, i), dp(i, i - 1)) for i in range(len(s)))

