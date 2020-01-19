class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        ranges = sorted([(max(i - r, 0), min(i + r, n)) for i, r in enumerate(ranges)])
        res = [(0, 0), (0, 0)]
        for r in ranges:
            if r[0] > res[-1][1]:
                break
            if r[1] <= res[-1][1]:
                continue
            while r[0] <= res[-2][1] and len(res) > 2:
                res.pop()
            res.append(r)
        if res[-1][1] >= n:
            return len(res) - 2
        else:
            return -1
