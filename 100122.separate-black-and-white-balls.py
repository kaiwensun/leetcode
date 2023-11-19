class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros = s.count("0")
        res = 0
        for c in s:
            if c == "0":
                zeros -= 1
            else:
                res += zeros
        return res

