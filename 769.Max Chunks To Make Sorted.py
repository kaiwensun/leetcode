class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        rval = 0
        target_min = target_max = 0
        met_min = met_max = False
        for i in xrange(len(arr)):
            met_min = met_min or arr[i] == target_min
            target_max = max(target_max, arr[i])
            if target_max == i and met_min:
                rval += 1
                target_min = target_max = i + 1
                met_min = met_max = False
        return rval
