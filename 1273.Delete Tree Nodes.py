class Solution(object):
    def deleteTreeNodes(self, nodes, parent, value):
        """
        :type nodes: int
        :type parent: List[int]
        :type value: List[int]
        :rtype: int
        """
        children = [[] for _ in xrange(nodes)]
        for child in xrange(len(parent)):
            if child != 0:
                children[parent[child]].append(child)
        isZero = [False] * nodes
        def dfsSum(node):
            s = value[node]
            for child in children[node]:
                s += dfsSum(child)
            if s == 0:
                isZero[node] = True
            return s
        def dfsCnt(node):
            if isZero[node]:
                return 0
            return sum(dfsCnt(child) for child in children[node]) + 1
        dfsSum(0)
        return dfsCnt(0)
