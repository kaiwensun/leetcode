import collections
class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s = cnt = 0
        for a in sorted(arr):
            s += a
            if s > 5000:
                break
            cnt += 1
        return cnt
