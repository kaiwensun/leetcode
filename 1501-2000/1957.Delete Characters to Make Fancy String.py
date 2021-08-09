class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for c in s:
            if len(res) >= 2 and res[-1] == res[-2] == c:
                continue
            res.append(c)
        return ''.join(res)

