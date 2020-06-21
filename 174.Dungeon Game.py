import functools
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dp(i, j):
            if not (0 <= i < len(dungeon) and 0 <= j < len(dungeon[i])):
                return float('inf')
            if i == len(dungeon) - 1and j == len(dungeon[i]) - 1:
                return max(-dungeon[i][j], 0) + 1
            return max(min(dp(i + 1, j), dp(i, j + 1)) - dungeon[i][j], 1)

        return dp(0, 0)
