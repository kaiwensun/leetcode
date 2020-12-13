class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        prefix_sum = [0] * (len(stones) + 1)
        for i in range(len(stones)):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        def get_sum(start, end):  # end exclusive
            return prefix_sum[end] - prefix_sum[start]
        @lru_cache(None)
        def dp(player, start, end):
            # 0 is Alice, 1 is Bob
            if start + 1 == end:
                return 0
            if player == 0:
                return max(dp(1 - player, start + 1, end) + get_sum(start + 1, end),
                           dp(1 - player, start, end - 1) + get_sum(start, end - 1))
            else:
                return min(dp(1 - player, start + 1, end) - get_sum(start + 1, end),
                           dp(1 - player, start, end - 1) - get_sum(start, end - 1))
        res = dp(0, 0, len(stones))
        dp.cache_clear()
        return res

