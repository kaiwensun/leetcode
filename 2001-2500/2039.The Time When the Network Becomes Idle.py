class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        distance = [None] * len(patience)
        queue = collections.deque([0, "#"])
        dist = 0
        while len(queue) > 1:
            u = queue.popleft()
            if u == "#":
                dist += 1
                queue.append(u)
                continue
            if distance[u] is not None:
                continue
            distance[u] = dist
            for v in graph[u]:
                if distance[v] is None:
                    queue.append(v)
        return max((distance[i] * 2 - 1) // patience[i] * patience[i] + distance[i] * 2 for i in range(1, len(patience))) + 1

