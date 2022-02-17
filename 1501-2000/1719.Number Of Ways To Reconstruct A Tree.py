from collections import Counter

class Solution(object):
    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(set)
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)
        roots = [x for x, partners in adj.iteritems() if len(partners) == len(adj) - 1]
        if not roots:
            return 0
        root = roots[0]
        can_swap = False
        for x, partners in adj.iteritems():
            if x == root:
                continue
            x_parent = None
            x_parent_influence = float("inf")
            for partner in partners:
                if len(adj[partner]) == len(partners):
                    can_swap = True
                if len(partners) <= len(adj[partner]) < x_parent_influence:
                    x_parent = partner
                    x_parent_influence = len(adj[partner])
            if not partners.issubset(adj[x_parent] | {x_parent}):
                return 0
        return 2 if can_swap else 1

