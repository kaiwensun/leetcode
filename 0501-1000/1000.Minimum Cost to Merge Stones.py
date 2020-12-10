from functools import lru_cache
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        if K != 2 and len(stones) % (K - 1) != 1:
            return -1
        if len(stones) == 1:
            return 0
        prefix_sum = [0] * (len(stones) + 1)
        for i in range(len(stones)):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        def get_sum_range(start, end):
            return prefix_sum[end] - prefix_sum[start]

        @lru_cache(None)
        def dp(start, end, group_size):
            if group_size == end - start:
                return 0
            if group_size == 1:
                res = get_sum_range(start, end) + dp(start, end, K)
            else:
                res = float("inf")
                for mid in range(start + 1, end):
                    res = min(res, dp(start, mid, 1) + dp(mid, end, group_size - 1))
            return res

        return dp(0, len(stones), 1)

