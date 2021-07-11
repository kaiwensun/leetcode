from collections import Counter, defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        l = Counter()
        r = Counter(s)
        seen = defaultdict(set)
        res = 0
        for mid in s:
            r[mid] -= 1
            if r[mid] == 0:
                del r[mid]
            additional = (set(l.keys()) & set(r.keys())) - seen[mid]
            res += len(additional)
            seen[mid] |= additional
            l[mid] += 1
        return res

