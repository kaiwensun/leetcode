import heapq

class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.available = list(range(1, n + 1))
        heapq.heapify(self.available)


    def reserve(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.available)


    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.available, seatNumber)



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

