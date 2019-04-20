import functools
class Solution:
    diffs = (
        (2, 1), (1, 2),
        (2, -1), (1, -2),
        (-2, 1), (-1, 2),
        (-2, -1), (-1, -2)
    )
    @functools.lru_cache(None)
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if not (0 <= r < N and 0 <= c < N):
            return 0
        if K == 0:
            return 1
        res = 0
        for dx, dy in self.diffs:
            res += self.knightProbability(N, K - 1, r + dx, c + dy)
        return res / float(8)
