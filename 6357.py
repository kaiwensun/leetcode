class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        l2r = []
        it = iter(t)
        pt = next(it, None)
        seen = 0
        for c in s:
            if c == pt:
                pt = next(it, None)
                if pt == None:
                    return 0
                seen += 1
            l2r.append(seen)
        mx = seen
        r2l = []
        it = iter(t[::-1])
        pt = next(it, None)
        seen = 0
        for c in reversed(s):
            r2l.append(seen)
            if c == pt:
                pt = next(it, None)
                seen += 1
        mx = max(mx, seen)
        r2l.reverse()
        return len(t) - max(mx, max(a + b for a, b in zip(l2r, r2l)))

