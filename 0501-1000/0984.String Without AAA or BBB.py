class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = []
        while A or B:
            if len(res) >= 2 and res[-2] == res[-1]:
                if res[-1] == "a":
                    res.append("b")
                    B -= 1
                else:
                    res.append("a")
                    A -= 1
            elif A < B:
                res.append("b")
                B -= 1
            elif A > B:
                res.append("a")
                A -= 1
            else:
                res.append("ab" * A)
                A = B = 0
        return "".join(res)

