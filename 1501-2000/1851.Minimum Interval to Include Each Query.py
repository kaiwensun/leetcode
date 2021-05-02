import heapq, bisect, collections

class Solution:
    
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        INF = 10 ** 8
        
        points = [(-1, True, INF)]
        for start, end in intervals:
            size = end - start + 1
            points.append((start, True, size))
            points.append((end + 1, False, size))
        sizes = []
        debt = collections.Counter()
        hist = [(-1, INF)]
        for point, is_start, size in sorted(points):
            if is_start:
                heapq.heappush(sizes, size)
            else:
                debt[size] += 1
            while sizes and debt[sizes[0]] != 0:
                debt[heapq.heappop(sizes)] -= 1
            min_size = sizes[0]
            if min_size != hist[-1][-1]:
                hist.append((point, min_size))
        res = []
        for query in queries:
            i = bisect.bisect_right(hist, (query, INF)) - 1
            size = hist[i][1]
            res.append(-1 if size == INF else size)
        return res

