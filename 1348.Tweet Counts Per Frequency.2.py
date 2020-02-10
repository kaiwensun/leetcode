import collections
class TweetCounts:

    def __init__(self):
        self.tweet2timeCounter = collections.defaultdict(collections.Counter)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweet2timeCounter[tweetName][time] += 1
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        intervals = {"minute": 60, "hour": 60 * 60, "day": 60 * 60 * 24}
        interval = intervals[freq]
        res = [0] * ((endTime - startTime) // interval + 1)
        counter = self.tweet2timeCounter[tweetName]
        for time, count in counter.items():
            if startTime <= time <= endTime:
                res[(time - startTime) // interval] += count
        return res
