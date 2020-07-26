import collections, heapq, functools
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:

        @functools.lru_cache(n)
        def priority(c):
            return max([priority(nxt) + 1 for nxt in graph[c]] + [0])
            
        graph = collections.defaultdict(list)
        cnt_pre = collections.Counter()
        for x, y in dependencies:
            graph[x - 1].append(y - 1)
            cnt_pre[y - 1] += 1
        heap = [(-priority(c), c) for c in range(n) if c not in cnt_pre]
        res = 0
        while heap:
            res += 1
            takings = []
            for _ in range(k):
                if not heap: break
                __, c = heapq.heappop(heap)
                takings.append(c)
            for taking in takings:
                for nxt in graph[taking]:
                    cnt_pre[nxt] -= 1
                    if cnt_pre[nxt] == 0:
                        heapq.heappush(heap, (-priority(nxt), nxt))
        return res
