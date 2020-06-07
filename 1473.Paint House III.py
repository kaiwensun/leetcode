from functools import lru_cache
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dp(i, color, target):
            if houses[i] != 0 and houses[i] != color:
                return float('inf')
            if target == 0:
                return float('inf')
            my_cost = cost[i][color - 1] if houses[i] == 0 else 0
            if i == 0:
                if target == 1:
                    return my_cost
                else:
                    return float('inf')
            other_cost = float('inf')
            
            for next_color in range(1, n + 1):
                other_cost = min(other_cost, dp(i - 1, next_color, target - int(next_color != color)))
            return my_cost + other_cost
        res = min(dp(m - 1, color, target) for color in range(1, n + 1))
        return res if res != float('inf') else -1
