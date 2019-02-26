class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        minimals = [0] * len(arr)
        minimals[-1] = float('inf')
        for i in xrange(len(arr) - 2, -1, -1):
            minimals[i] = min(arr[i + 1], minimals[i + 1])
        rval = 0
        maximal = arr[0]
        for i in xrange(len(arr)):
            maximal = max(maximal, arr[i])
            if maximal <= minimals[i]:
                rval += 1
        return rval
        
