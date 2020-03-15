import heapq
class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        data = sorted(zip(efficiency, speed), reverse=True)
        speed_heap = []
        total_speed = 0
        performance = 0
        for eff, spd in data:
            heapq.heappush(speed_heap, spd)
            total_speed += spd
            if len(speed_heap) > k:
                total_speed -= heapq.heappop(speed_heap)
            performance = max(performance, total_speed * eff)
        return performance % (10 ** 9 + 7)
