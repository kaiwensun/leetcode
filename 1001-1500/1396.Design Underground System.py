import collections
class UndergroundSystem(object):

    def __init__(self):
        self.onboard = {}
        self.records = collections.defaultdict(lambda: [0, 0])
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.onboard[id] = (stationName, t)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStation, startTime = self.onboard.pop(id)
        totalTime, totalCnt = self.records[startStation, stationName]
        self.records[startStation, stationName] = [totalTime + t - startTime, totalCnt + 1]
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        totalTime, totalCnt = self.records[startStation, endStation]
        return totalTime / float(totalCnt)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
