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

        def rightHasApple(i, j):
            if i == m - 1:
                return remainsApple[i][j] > 0
            else:
                return remainsApple[i][j] - remainsApple[i + 1][j] > 0
        def belowHasApple(i, j):
            if j == n - 1:
                return remainsApple[i][j] > 0
            else:
                return remainsApple[i][j] - remainsApple[i][j + 1] > 0

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
                seenAppleOnRight = seenAppleOnRight or rightHasApple(new_i - 1, j)
                if seenAppleOnRight:
                    res += dp(remainPieces - 1, new_i, j)
                    res %= MOD
            seenAppleBelow = False
            for new_j in range(j + 1, n):
                seenAppleBelow = seenAppleBelow or belowHasApple(i, new_j - 1)
                if seenAppleBelow:
                    res += dp(remainPieces - 1, i, new_j)
                    res %= MOD
            return res

        return dp(k, 0, 0)
                
