from collections import defaultdict
class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = set()
        def dfs(root):
            res = 0
            if root not in visited:
                visited.add(root)
                for nbr in graph[root]:
                    res += dfs(nbr)
                if res or hasApple[root]:
                    res += 2
            return res
        return max(0, dfs(0) - 2)
