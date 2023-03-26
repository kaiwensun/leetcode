from collections import defaultdict

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        if len(coins) <= 3 or sum(coins) <= 1:
            return 0

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs_clean_empty_subtrees(node, parent):
            has_coin = coins[node] == 1
            for nxt in list(graph[node]):
                if nxt == parent:
                    continue
                if dfs_clean_empty_subtrees(nxt, node):
                    has_coin = True
                else:
                    graph[node].remove(nxt)
                    graph[nxt].remove(node)
            return has_coin

        def dfs_trim_leaves(node, parent):
            if len(graph[node]) == 1:
                graph[node].remove(parent)
                graph[parent].remove(node)
                return
            for nxt in list(graph[node]):
                if nxt == parent:
                    continue
                dfs_trim_leaves(nxt, node)

        root = coins.index(1)
        dfs_clean_empty_subtrees(root, None)

        for _ in range(2):
            root = next(iter(leaf for leaf, neighbors in graph.items() if len(neighbors) > 1), None)
            if root is None:
                return 0
            dfs_trim_leaves(root, None)

        remain_edges = sum(len(v) for v in graph.values())
        return remain_edges

