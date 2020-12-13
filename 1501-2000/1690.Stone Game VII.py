class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        prefix_sum = [0] * (len(stones) + 1)
        for i in range(len(stones)):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        def get_sum(start, end):
            return prefix_sum[end] - prefix_sum[start]
        dp = [[None] * len(stones) for _ in range(len(stones))]

        def dfs(player, start, end):
            if dp[start][end - 1] is not None:
                return dp[start][end - 1]
            if start + 1 == end:
                return 0
            if player == 0:
                res = max(dfs(1 - player, start + 1, end) + get_sum(start + 1, end),
                          dfs(1 - player, start, end - 1) + get_sum(start, end - 1))
            else:
                res = min(dfs(1 - player, start + 1, end) - get_sum(start + 1, end),
                          dfs(1 - player, start, end - 1) - get_sum(start, end - 1))
            dp[start][end - 1] = res
            return res
        return dfs(0, 0, len(stones))

