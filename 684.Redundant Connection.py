class UnionFind():
    def __init__(self):
        self._parent = {}

    def find(self, u):
        self._parent.setdefault(u, u)
        if self._parent[u] != u:
            self._parent[u] = self.find(self._parent[u])
        return self._parent[u]
    
    def union(self, u, v):
        u_parent = self.find(u)
        v_parent = self.find(v)
        self._parent[u_parent] = v_parent

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind()
        for u, v in edges:
            u_parent = uf.find(u)
            v_parent = uf.find(v)
            if u_parent == v_parent:
                return [u, v]
            uf.union(u, v)
        assert(False)
