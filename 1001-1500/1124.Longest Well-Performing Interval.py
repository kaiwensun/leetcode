class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        points = [1 if x > 8 else -1 for x in hours]
        seen = {0: -1}
        benefit = 0
        res = 0
        for i, point in enumerate(points):
            benefit += point
            seen.setdefault(benefit, i)
            if benefit > 0:
                res = max(res, i + 1)
            else:
                res = max(res, i - seen.get(benefit - 1, float('inf')))
        print seen
        return res
