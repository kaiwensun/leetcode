class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        nodes = [True] * n
        for src, dst in edges:
            nodes[dst] = False
        return [i for i, no_src in enumerate(nodes) if no_src]

