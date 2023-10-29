from functools import cache
from collections import defaultdict

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        @cache
        def get_halves(i, parent):
            coin = coins[i]
            cnt = Counter()
            cuts = 0
            while coin:
                cnt[cuts] = coin
                coin >>= 1
                cuts += 1
            for child in graph[i]:
                if child == parent:
                    continue
                cnt += get_halves(child, i)
            return cnt

        @cache
        def dp(i, parent, cuts):
            cnt = get_halves(i, parent)
            coin = coins[i]
            if cnt[cuts] == 0:
                return 0
            return max(
                (coin >> cuts) - k + sum(dp(child, i, cuts) for child in graph[i] if child != parent),
                (coin >> (cuts + 1)) + sum(dp(child, i, cuts + 1) for child in graph[i] if child != parent)
            )
        return dp(0, -1, 0)

