import collections, bisect
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.store[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        index = bisect.bisect_left(self.store[key], (timestamp + 1, )) - 1
        if index >= 0:
            return self.store[key][index][1]
        return ""


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

