import collections, functools

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:

        def find_path(node, target, parent, path):
            path.append(node)
            if node == target:
                return path
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                found = find_path(nxt, target, node, path)
                if found:
                    return found
            path.pop()

        @functools.cache
        def dp(node, parent, parent_is_halved):
            res1 = price[node] * count[node]
            subtree_price = float("inf")
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                res1 += dp(nxt, node, False)
            res2 = float("inf")
            if not parent_is_halved:
                res2 = price[node] // 2 * count[node]
                for nxt in graph[node]:
                    if nxt == parent:
                        continue
                    res2 += dp(nxt, node, True)
            return min(res1, res2)

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [0] * n
        for start, end in trips:
            path = find_path(start, end, -1, [])
            for node in path:
                count[node] += 1

        return dp(0, -1, False)

