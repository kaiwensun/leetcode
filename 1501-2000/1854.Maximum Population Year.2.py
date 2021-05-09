import collections

class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        diffs = collections.Counter()
        for start, end in logs:
            diffs[start] += 1
            diffs[end] -= 1
        mx_cnt = cnt = 0
        res = None
        for year, diff in sorted(diffs.items()):
            cnt += diff
            if cnt > mx_cnt:
                res, mx_cnt = year, cnt
        return res

