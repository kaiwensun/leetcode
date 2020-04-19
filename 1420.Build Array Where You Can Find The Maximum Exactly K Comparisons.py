import functools
class Solution:

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @functools.lru_cache(None)
        def dp(index, max_value, remaining_cost):
            if max_value == 0 and index != 0:
                return 0
            if index == n - 1:
                if remaining_cost == 0:
                    return max_value
                if max_value < m and remaining_cost == 1:
                    return m - max_value
                return 0
            if n - index + 1 < remaining_cost:
                return 0
            if m - max_value < remaining_cost:
                return 0
            res = max_value * dp(index + 1, max_value, remaining_cost)
            for new_max_value in range(max_value + 1, m + 1):
                res += dp(index + 1, new_max_value, remaining_cost - 1)
            return res % 1000000007
        return dp(0, 0, k)
    
        
