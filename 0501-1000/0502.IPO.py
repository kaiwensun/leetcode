import heapq
class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        capital_queue = zip(Capital, Profits)
        heapq.heapify(capital_queue)
        profit_queue = []
        for i in xrange(k):
            while capital_queue and capital_queue[0][0] <= W:
                _, p = heapq.heappop(capital_queue)
                heapq.heappush(profit_queue, -p)
            if not profit_queue:
                break
            W -= heapq.heappop(profit_queue)
        return W

