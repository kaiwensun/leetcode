from itertools import chain
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        c2n = {}
        for u, v in equations:
            c2n.setdefault(u, len(c2n))
            c2n.setdefault(v, len(c2n))
        size = len(c2n)
        dp = [[None] * size for _ in xrange(size)]
        for eq, value in zip(equations, values):
            u, v = eq
            dp[c2n[u]][c2n[v]] = value
            dp[c2n[v]][c2n[u]] = 1 / value
        for u in xrange(size):
            dp[u][u] = 1.0
        for k in xrange(size):
            for u in xrange(size):
                for v in xrange(size):
                    if dp[u][v] is None and dp[u][k] is not None and dp[k][v] is not None:
                        dp[u][v] = dp[u][k] * dp[k][v]
                
        res = []
        for u, v in queries:
            if u in c2n and v in c2n and dp[c2n[u]][c2n[v]] is not None:
                res.append(dp[c2n[u]][c2n[v]])
            else:
                res.append(-1.0)
        return res

