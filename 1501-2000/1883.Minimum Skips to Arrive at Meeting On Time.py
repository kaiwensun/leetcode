import functools, math

INF_TIME = 10 ** 8 + 1
EPSILON = 1e-8

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        
        @functools.lru_cache(None)
        def dp(skip, posi):
            if skip < 0:
                return INF_TIME
            if posi == -1:
                return 0
            return min(math.ceil(dp(skip, posi - 1) - EPSILON) + dist[posi] / speed,
                       dp(skip - 1, posi - 1) + dist[posi] / speed)
        
        for skip in range(len(dist)):
            if dp(skip, len(dist) - 1) <= hoursBefore + EPSILON:
                return skip
        return -1

