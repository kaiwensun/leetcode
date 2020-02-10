import bisect, collections
class TweetCounts(object):

    def __init__(self):
        self.tweet2code = {}
        self.times = []
        self.time2codes = collections.defaultdict(collections.Counter)

    def code(self, tweetName):
        return self.tweet2code.setdefault(tweetName, len(self.tweet2code))

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        code = self.code(tweetName)
        index = bisect.bisect_left(self.times, time)
        if index == len(self.times) or self.times[index] != time:
            bisect.insort(self.times, time)
        self.time2codes[time][code] += 1
            
        
    freq2interval = {
        "minute": 60,
        "hour": 60 * 60,
        "day": 60 * 60 * 24
    }
        

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        interval = self.freq2interval[freq]
        size = (endTime - startTime) // interval + 1;
        res = [0] * size
        index = bisect.bisect_left(self.times, startTime)
        code = self.code(tweetName)
        while index < len(self.times) and self.times[index] <= endTime:
            time = self.times[index]
            resIndex = (time - startTime) // interval
            res[resIndex] += self.time2codes[time][code]
            index += 1
        return res
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
