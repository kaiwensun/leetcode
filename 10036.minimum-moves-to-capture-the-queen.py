class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        def helper(a, b, c, d, e, f):
            if a == e:
                if c != e or (not b < d < f and not f < d < b):
                    return 1
            if c - e == d - f:
                if a - c != b - d or (not c < a < e and not e < a < c):
                    return 1
            return 2
        def trans(x, y):
            return y, 9 - x
        res1 = helper(a, b, c, d, e, f)
        res2 = helper(*trans(a, b), *trans(c, d), *trans(e, f))
        return min(res1, res2)

