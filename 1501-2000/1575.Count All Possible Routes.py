from functools import lru_cache
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dp(cur, fuel):
            res = int(cur == finish)
            for i in range(cur - 1, -1, -1):
                if locations[cur] - locations[i] > fuel:
                    break
                res += dp(i, fuel - (locations[cur] - locations[i]))
            for i in range(cur + 1, len(locations)):
                if locations[i] - locations[cur] > fuel:
                    break
                res += dp(i, fuel - (locations[i] - locations[cur]))
            return res % MOD
        MOD = 10 ** 9 + 7
        start_loc, finish_loc = locations[start], locations[finish]
        locations.sort()
        start = locations.index(start_loc)
        finish = locations.index(finish_loc)
        return dp(start, fuel)

