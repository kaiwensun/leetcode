import collections
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt = collections.Counter(arr)
        res = float("-inf")
        for k, v in cnt.items():
            if k == v:
                res = max(res, v)
        return -1 if res == float("-inf") else res
