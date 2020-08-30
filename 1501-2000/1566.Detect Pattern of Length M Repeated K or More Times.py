class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        for start in xrange(len(arr)):
            end = start + m * k
            if end > len(arr):
                break
            for i in xrange(start + m, end):
                if arr[i] != arr[i - m]:
                    break
            else:
                return True
        return False
