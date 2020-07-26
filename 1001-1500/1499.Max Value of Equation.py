import heapq
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap = [] # element: (- (yi - xi), xi)
        res = float('-inf')
        for xj, yj in points:
            while heap and xj - heap[0][1] > k:
                heapq.heappop(heap)
            if heap:
                yi_xi = -heap[0][0]
                res = max(res, yi_xi + yj + xj)
            heapq.heappush(heap, (xj - yj, xj))
        return res
