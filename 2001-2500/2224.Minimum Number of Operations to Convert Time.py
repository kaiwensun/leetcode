class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def toSeconds(t):
            t = map(int, t.split(":"))
            return next(t) * 60 + next(t)

        diff = toSeconds(correct) - toSeconds(current)
        res = 0
        for sub in [60, 15, 5, 1]:
            res += diff // sub
            diff = diff % sub
        return res

