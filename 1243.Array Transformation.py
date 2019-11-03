class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for _ in xrange(min(arr), max(arr) + 2):
            arr = arr[:1] + [b + (a > b < c) - (a < b > c) for a, b, c in zip(arr[:-2], arr[1:len(arr) - 1], arr[2:])] + arr[-1:]
        return arr
