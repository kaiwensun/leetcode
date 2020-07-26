import functools
class Solution(object):
    keyboard = []
    key2cord = {}
    
    def initKeyboard(self):
        if self.keyboard:
            return
        self.keyboard = [
            "ABCDEF",
            "GHIJKL",
            "MNOPQR",
            "STUVWX",
            "YZ"
        ]
        for i in range(len(self.keyboard)):
            for j in range(len(self.keyboard[i])):
                self.key2cord[self.keyboard[i][j]] = (i, j)

    def minimumDistance(self, word):
        def dist(a, b):
            ax, ay = self.key2cord[a]
            bx, by = self.key2cord[b]
            return abs(ax - bx) + abs(ay - by)
        
        @functools.lru_cache(None)
        def oneFingerStrike(start, end):
            if start >= end:
                return 0
            return oneFingerStrike(start, end - 1) + dist(word[end - 1], word[end])
        @functools.lru_cache(None)
        def dp(left, right):
            if left >= right:
                assert(False)
            if left == 0:
                res = oneFingerStrike(1, right)
            elif right < 2:
                res = 0
            elif left == right - 1:
                res = min(dp(i, left) + dist(word[i], word[right]) for i in range(left))
                res = min(res, oneFingerStrike(0, left))
            else:
                res = dp(left, left + 1) + oneFingerStrike(left + 1, right)       
            return res
        
        self.initKeyboard()
        return min(dp(left, len(word) - 1) for left in range(len(word) - 1))
