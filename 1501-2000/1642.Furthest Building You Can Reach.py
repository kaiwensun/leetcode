import heapq
class Solution(object):
    
    def furthestBuilding(self, heights, bricks, ladders, cur=0):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        gains = []
        for i in xrange(len(heights) - 1):
            gain = heights[i + 1] - heights[i]
            if gain <= 0:
                continue
            heapq.heappush(gains, gain)
            if len(gains) > ladders:
                bricks -= heapq.heappop(gains)
                if bricks < 0:
                    return i
        return len(heights) - 1

