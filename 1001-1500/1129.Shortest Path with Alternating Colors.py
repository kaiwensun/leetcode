class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        answer = [float('inf')] * n
        red_edges_map = collections.defaultdict(set)
        blue_edges_map = collections.defaultdict(set)
        for u, v in red_edges:
            red_edges_map[u].add(v)
        for u, v in blue_edges:
            blue_edges_map[u].add(v)
        visited = set(((0, 0), (0, 1))) # (point, starting color)
        queue = collections.deque(((0, 0, 0), (0, 1, 0))) # (src, starting color, dist)
        answer[0] = 0
        while queue:
            point = queue.popleft()
            edges_map = red_edges_map if point[1] == 0 else blue_edges_map
            for target in edges_map[point[0]]:
                if (target, 1 - point[1]) in visited:
                    continue
                answer[target] = min(answer[target], point[2] + 1)
                visited.add((target, 1 - point[1]))
                queue.append((target, 1 - point[1], point[2] + 1))
        for i in xrange(len(answer)):
            if answer[i] == float('inf'):
                answer[i] = -1
        return answer
