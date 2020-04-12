class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        res = []
        P = range(1, m + 1)
        for query in queries:
            index = P.index(query)
            res.append(index)
            P = [P[index]] + P[:index] + P[index + 1:]
        return res
