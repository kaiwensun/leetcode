class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        rval = 0
        maximal = 0
        for i in xrange(len(arr)):
            maximal = max(maximal, arr[i])
            if maximal == i:
                rval += 1
        return rval
