from collections import Counter

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        res = acc = 0
        seen = Counter()
        seen[0] = 1
        for c in word:
            acc ^= 1 << (ord(c) - ord('a'))
            target = 1
            res += seen[acc]
            for _ in range(10):
                res += seen[acc ^ target]
                target <<= 1
            seen[acc] += 1
        return res

