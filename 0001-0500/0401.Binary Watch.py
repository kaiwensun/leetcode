from collections import defaultdict

class Solution(object):
    minutes = defaultdict(list)
    hours = defaultdict(list)
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def init():
            if not self.minutes:
                for minute in xrange(60):
                    self.minutes[cntDigit(minute)].append(minute)
                for hour in xrange(12):
                    self.hours[cntDigit(hour)].append(hour)
        def cntDigit(d):
            cnt = 0
            while d:
                d &= d - 1
                cnt += 1
            return cnt
        init()
        res = []
        for hr in xrange(num + 1):
            for bit_hr in self.hours[hr]:
                for bit_min in self.minutes[num - hr]:
                    res.append("%d:%02d" % (bit_hr, bit_min))
        return res
