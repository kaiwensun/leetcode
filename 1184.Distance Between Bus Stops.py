class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        s = sum(distance)
        res1 = sum(distance[min(start, destination): max(start, destination) + 1])
        return min(res1, )
