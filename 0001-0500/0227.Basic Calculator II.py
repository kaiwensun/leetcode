class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        calcs = {
            "+": int.__add__,
            "-": int.__sub__,
            "*": int.__mul__,
            "/": int.__div__
        }
        
        def tokenize(s):
            res = ""
            for c in s:
                if c == " ":
                    continue
                elif c in "+-*/":
                    yield (int(res), calcs[c])
                    res = ""
                else:
                    res += c
            yield int(res), None

        res = 0
        op = calcs["+"]
        token_gen = tokenize(s)
        while op:
            num, nextop = next(token_gen)
            while nextop in [calcs["*"], calcs["/"]]:
                num2, nextop2 = next(token_gen)
                num = nextop(num, num2)
                nextop = nextop2
            res = op(res, num)
            op = nextop
        return res

