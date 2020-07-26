import heapq
class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        heap = []
        seen = {}
        next_rain = [None] * len(rains)
        res = [-1] * len(rains)
        for i in xrange(len(rains) - 1, -1, -1):
            if rains[i]:
                lake = rains[i]
                next_rain[i] = seen.get(lake)
                seen[lake] = i
        for i in xrange(len(next_rain)):
            if rains[i]:
                if next_rain[i] is not None:
                    heapq.heappush(heap, next_rain[i])
            else:
                if heap:
                    rain_id = heapq.heappop(heap)
                    res[i] = rains[rain_id]
                else:
                    res[i] = 1
            if heap and heap[0] <= i:
                return []
        return res
