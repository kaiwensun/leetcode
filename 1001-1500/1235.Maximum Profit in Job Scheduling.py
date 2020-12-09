import heapq
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        heap = []  # (endTime, totalProfilt)
        res = 0
        for s, e, p in sorted(zip(startTime, endTime, profit)):
            while heap and heap[0][0] <= s:
                _, pre_profit = heapq.heappop(heap)
                res = max(res, pre_profit)
            heapq.heappush(heap, (e, res + p))
        for _, pre_profit in heap:
            res = max(res, pre_profit)
        return res

