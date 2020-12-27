import heapq
class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        queue = []
        res = 0
        for i in xrange(len(days) + max(days)):
            while queue and (queue[0][0] < i or queue[0][1] == 0):
                heapq.heappop(queue)
            if i < len(days) and apples[i]:
                heapq.heappush(queue, (i + days[i] - 1, apples[i]))
            if queue:
                res += 1
                heapq.heapreplace(queue, (queue[0][0], queue[0][1] - 1))
            if i >= len(days) and not queue:
                break
        return res

