from collections import defaultdict
import heapq

MOD = 10 ** 9 + 7

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append([v, t])
            graph[v].append([u, t])
        
        dp = [None] * n  # [min_time, number_of_ways]
        dp[0] = [0, 1]
        queue = [[0, 0]] # [min_time, node]
        while queue:
            min_time, u = heapq.heappop(queue)
            for v, t in graph[u]:
                if dp[v] is None:
                    dp[v] = [min_time + t, dp[u][1]]
                    heapq.heappush(queue, [min_time + t, v])
                elif dp[v][0] == min_time + t:
                    dp[v][1] += dp[u][1]
        return dp[n - 1][1] % MOD

