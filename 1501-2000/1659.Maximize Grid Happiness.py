from functools import lru_cache
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        INTRO, EXTRO, LOSS, GAIN = 120, 40, -30, 20
        INITIAL = {
            " ": 0,
            "i": INTRO,
            "e": EXTRO
        }

        def getAdjustedHappiness(c1, c2):
            c1, c2 = sorted([c1, c2])
            if c1 == " ":
                return 0
            if c1 == "e":
                if c2 == "e": return GAIN + GAIN
                if c2 == "i": return GAIN + LOSS
            if c1 == "i":
                return LOSS + LOSS
            assert(False)
        
        @lru_cache(None)
        def dp(visible_row, i, j, introvertsCount, extrovertsCount):
            if introvertsCount == extrovertsCount == 0 or i < 0 or j < 0:
                return 0
            res = 0
            visible_row = list(visible_row)
            availables = [" "]
            if introvertsCount: availables.append("i")
            if extrovertsCount: availables.append("e")
            for value in availables:
                cur_res = INITIAL[value] + getAdjustedHappiness(value, visible_row[j]) + getAdjustedHappiness(value, visible_row[j + 1])
                buff = visible_row[j]
                visible_row[j] = value
                cur_res += dp(tuple(visible_row), i + ((j - 1) // n), (j - 1) % n, introvertsCount - int(value == "i"), extrovertsCount - int(value == "e"))
                visible_row[j] = buff
                res = max(res, cur_res)
            return res

        return dp(" " * (n + 1), m - 1, n - 1, introvertsCount, extrovertsCount)

