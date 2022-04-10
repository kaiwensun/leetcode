class Solution:
    def minimizeResult(self, expression: str) -> str:
        a, b = expression.split("+")
        def calc(l, r):
            if l == len(a) and r == 0:
                return float("inf")
            a1, a2 = a[:l], a[l:]
            b1, b2 = b[:r], b[r:]
            a1 = int(a1 or "1")
            a2 = int(a2 or "0")
            b1 = int(b1 or "0")
            b2 = int(b2 or "1")
            return a1 * (a2 + b1) * b2
        res = float("inf")
        for l in range(len(a)):
            for r in range(1, len(b) + 1):
                c = calc(l, r)
                if res > c:
                    res = c
                    res_exp = f"{a[:l]}({a[l:]}+{b[:r]}){b[r:]}"
        return res_exp

