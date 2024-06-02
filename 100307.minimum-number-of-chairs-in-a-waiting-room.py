class Solution:
    def minimumChairs(self, s: str) -> int:
        res = cur = 0
        for c in s:
            cur += 1 if c == 'E' else -1
            res = max(res, cur)
        return res

