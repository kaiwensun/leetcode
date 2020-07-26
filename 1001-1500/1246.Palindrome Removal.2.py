# This solution exceeds time limit. But it is intuitive. See another DP solution wihout recursion.

import functools
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        INF = 100
        @functools.lru_cache(None)       
        def dp(start, end):
            if start >= end:
                return 1
            if arr[start] == arr[end]:
                return dp(start + 1, end - 1)
            return min(dp(start, split) + dp(split + 1, end) for split in range(start, end))
        return dp(0, len(arr) - 1)
