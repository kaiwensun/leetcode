class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        buckets = [0] * (n + 1)
        for citation in citations:
            buckets[min(citation, n)] += 1
        sm = 0
        for i in xrange(n, -1, -1):
            sm += buckets[i]
            if sm >= i:
                return i

