import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller = [-float("inf")]
        self.bigger = [float("inf")]


    def addNum(self, num: int) -> None:
        heapq.heapppush(self.smaller, -num)
        if len(self.smaller) - len(self.bigger) > 1:
            heapq.heappush(self.bigger, -heapq.heappop(self.smaller))
        if -self.smaller[0] > self.bigger[0]:
            heapq.heapreplace(self.smaller, -heapq.heapreplace(self.bigger, -self.smaller[0]))


    def findMedian(self) -> float:
        if len(self.smaller) == len(self.bigger):
            return (-self.smaller[0] + self.bigger[0]) / 2
        else:
            return -self.smaller[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

