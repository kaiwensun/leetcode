import functools
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        MOD = 10 ** 9 + 7
        remainsApple = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            rightApple = 0
            for j in range(n - 1, -1, -1):
                if pizza[i][j] == "A":
                    rightApple += 1
                remainsApple[i][j] = (remainsApple[i + 1][j] if i != m - 1 else 0) + rightApple

        @functools.lru_cache(None)
        def dp(remainPieces, i, j):
            if remainPieces == 1:
                return 1 if remainsApple[i][j] > 0 else 0
            if remainsApple[i][j] < remainPieces:
                return 0
            if i == m - 1 and j == n - 1:
                assert(False)
            res = 0
            seenAppleOnRight = False
            for new_i in range(i + 1, m):
                if remainsApple[i][j] != remainsApple[new_i][j]:
                    res += dp(remainPieces - 1, new_i, j)
                    res %= MOD
            for new_j in range(j + 1, n):
                if remainsApple[i][j] != remainsApple[i][new_j]:
                    res += dp(remainPieces - 1, i, new_j)
                    res %= MOD
            return res
        return dp(k, 0, 0)
