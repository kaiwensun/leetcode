class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = float("inf")
        res = []
        for i in xrange(1, len(arr)):
            if arr[i] - arr[i - 1] < min_diff:
                min_diff = arr[i] - arr[i - 1]
                res = []
            if arr[i] - arr[i - 1] == min_diff:
                res.append([arr[i - 1], arr[i]])
        return res

