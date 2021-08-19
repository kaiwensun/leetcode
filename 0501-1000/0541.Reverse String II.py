class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        for i in range(0, len(s), 2 * k):
            res.append(s[i + k - 1 : max(0, i - 1) or None : -1] + s[i + k: i + 2 * k])
        return "".join(res)

