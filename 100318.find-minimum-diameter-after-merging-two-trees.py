# To get a tree diameter, do to round of DFS.
# Round 1 start from a random node to find the farthest node, which must be one end of the diameter
# Round 2 start from the one end of the diameter to find the other end of the diameter.

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def get_diameter(edges):
            if not edges:
                return 0
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            def dfs(node, parent):
                # return longest path length and farthest node
                res = [0, node]
                for neighbor in graph[node]:
                    if neighbor == parent:
                        continue
                    res = max(res, dfs(neighbor, node))
                res[0] += 1
                return res
            _, end_node = dfs(0, -1)
            diameter, _ = dfs(end_node, -1)
            return diameter - 1

        diameter1 = get_diameter(edges1)
        diameter2 = get_diameter(edges2)
        radius1 = (diameter1 + 1) // 2
        radius2 = (diameter2 + 1) // 2
        return max(radius1 + radius2 + 1, diameter1, diameter2)

