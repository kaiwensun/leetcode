import functools
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @functools.lru_cache(None)
        def take(start, M):
            if start + 2 * M >= len(piles):
                return sum(piles[start:])
            taken = 0
            res = float('-inf')
            for i in range(start, start + 2 * M):
                taken += piles[i]
                consequence = take(i + 1, max(M, i - start + 1))
                res = max(res, taken - consequence)
            return res
        return (sum(piles) + take(0, 1)) // 2
