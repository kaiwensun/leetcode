from collections import Counter, defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        l = Counter()
        r = Counter(s)
        seen = defaultdict(set)
        for mid in s:
            r[mid] -= 1
            if r[mid] == 0:
                del r[mid]
            seen[mid] |= (set(l.keys()) & set(r.keys()))
            l[mid] += 1
        return sum(map(len, seen.values()))

