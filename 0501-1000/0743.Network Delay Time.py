class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = [[] for _ in xrange(N)]
        for u, v, w in times:
            graph[u - 1].append((v - 1, w))
        visited = [False] * N
        heap = [(0, K - 1)]
        res = 0
        cnt = 0
        while heap:
            dist, node = heapq.heappop(heap)
            if visited[node]:
                continue
            res = max(res, dist)
            visited[node] = True
            for neighbor, w in graph[node]:
                if visited[neighbor]:
                    continue
                heapq.heappush(heap, (dist + w, neighbor))
        return res if all(visited) else -1

