import heapq, collections

class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        shortest_time = None
        visited = collections.defaultdict(set)
        # visited[0] = 1
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        heap = [(0, 1)] # [(time_to_leave_the_node, node), ...]
        while heap:
            t, u = heapq.heappop(heap)
            if len(visited[u]) >= 2 or t in visited[u]:
                continue
            visited[u].add(t)
            next_arrive_time = t + time
            next_leave_time = next_arrive_time if (next_arrive_time // change % 2 == 0) else (next_arrive_time // change + 1) * change
            for v in graph[u]:
                if v == n:
                    if shortest_time != None and next_arrive_time > shortest_time:
                        return next_arrive_time
                    shortest_time = next_arrive_time
                if len(visited[v]) >= 2 or next_leave_time in visited[v]:
                    continue
                heapq.heappush(heap, (next_leave_time, v))

