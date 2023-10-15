class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        def minimum(s1, s2):
            if len(s1) == len(s2):
                return min(s1, s2)
            return s1 if len(s1) < len(s2) else s2

        res = "2" * len(s)
        l = 0
        for r in range(len(s)):
            if s[r] == "0":
                continue
            k -= 1
            if k == 0:
                while k == 0:
                    if s[l] == "1":
                        k += 1
                    l += 1
                res = minimum(res, s[l - 1: r + 1])
        return "" if res[0] == "2" else res

