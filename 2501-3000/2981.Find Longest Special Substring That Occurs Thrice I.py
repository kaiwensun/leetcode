from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        cnt = defaultdict(list)
        l = s[0]
        n = 0
        for c in s:
            if c != l:
                cnt[l].append(n)
                l = c
                n = 0
            n += 1
        cnt[l].append(n)
        res = 0
        for counts in cnt.values():
            counts.sort()
            res = max(res, counts[-1] - 2)
            if len(counts) >= 2:
                res = max(res, min(counts[-1] - 1, counts[-2]))
            if len(counts) >= 3:
                res = max(res, counts[-3])
        return res or -1

