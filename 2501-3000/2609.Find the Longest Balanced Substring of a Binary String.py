class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = 0
        prev = '1'
        cnts = [0, 0]
        for c in s:
            if prev == '1' and c == '0':
                cnts[0] = cnts[1] = 0
            cnts[int(c)] += 1
            res = max(res, min(cnts))
            prev = c
        return res * 2

