class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        all_num = "123456789"
        def seqOfLength(length):
            if not (0 < length < 10):
                return []
            return map(int, [all_num[start:start + length] for start in xrange(0, 10 - length)])

        res = []
        for length in xrange(len(str(low)), len(str(high)) + 1):
            res.extend(filter(lambda n: low <= n <= high, seqOfLength(length)))
        return res

