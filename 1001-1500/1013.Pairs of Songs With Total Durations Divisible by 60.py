class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        counter = collections.Counter([t % 60 for t in time])
        rval = counter[0] * (counter[0] - 1) / 2
        rval += counter[30] * (counter[30] - 1) / 2
        for k, v in counter.items():
            if 0 < k < 30:
                rval += counter[k] * counter[60 - k]
        return rval
