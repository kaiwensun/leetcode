from collections import defaultdict

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        prev_size = {}
        for i in range(len(s)):
            res = 0
            for prev_ord in range(max(ord('a'), ord(s[i]) - k), min(ord('z'), ord(s[i]) + k) + 1):
                res = max(res, prev_size.get(prev_ord, 0))
            prev_size[ord(s[i])] = res + 1
        return max(prev_size.values())

