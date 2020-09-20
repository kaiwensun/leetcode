from functools import lru_cache
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        group2_best_friends = [min(cost[i][j] for i in range(m)) for j in range(n)]

        @lru_cache(None)
        def dp(group1_index, group2_mask):
            if group1_index == -1:
                return sum(group2_best_friends[j] for j in range(n) if group2_mask & (1 << j) == 0)
            return min(cost[group1_index][j] + dp(group1_index - 1, group2_mask | (1 << j)) for j in range(n))
        return dp(m - 1, 0)

