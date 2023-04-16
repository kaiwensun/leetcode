class Solution:
    def addMinimum(self, word: str) -> int:
        res = 0
        wanted = 0
        for c in word + "a":
            diff = ((ord(c) - ord('a') + 3) - wanted) % 3
            res += diff
            wanted += diff + 1
            wanted %= 3
        return res

