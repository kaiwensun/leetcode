from functools import lru_cache
from collections import defaultdict
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(request_id, mismatch):
            res = float("-inf")
            if request_id < 0:
                return 0 if all(mis == 0 for mis in mismatch) else float("-inf")
            new_mismatch = list(mismatch)
            f, t = requests[request_id]
            new_mismatch[f] -= 1
            new_mismatch[t] += 1
            return max(dp(request_id - 1, mismatch), dp(request_id - 1, tuple(new_mismatch)) + 1)
        return dp(len(requests) - 1, (0,) * n)

