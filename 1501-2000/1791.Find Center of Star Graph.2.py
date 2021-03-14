from collections import defaultdict

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        for u in edges[0]:
            if u in edges[1]:
                return u
        assert(False)

