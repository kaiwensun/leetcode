import heapq

"""
思路: 用binary test 处理min-max或者max-min问题。特别是当目标答案的搜索范围特别大时。
"""

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        mx_cost = 0
        graph = defaultdict(list)
        for u, v, cost in edges:
            if online[u] and online[v]:
                mx_cost = max(mx_cost, cost)
                graph[u].append([v, cost])

        def test(score):
            # only edges of cost gte the score are considered valid
            # [[path cost from 0, node id], ...]
            queue = [[0, 0]]
            visited = set()
            while queue:
                path_cost, node = heapq.heappop(queue)
                if node in visited:
                    continue
                visited.add(node)
                for nxt_node, nxt_edge_cost in graph[node]:
                    if nxt_edge_cost < score:
                        continue
                    if path_cost + nxt_edge_cost > k:
                        continue
                    if nxt_node in visited:
                        continue
                    if nxt_node == n - 1:
                        return True
                    heapq.heappush(queue, [path_cost + nxt_edge_cost, nxt_node])
            return False

        l, r = 0, mx_cost + 1
        while l < r:
            mid = (l + r) // 2
            if test(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1

