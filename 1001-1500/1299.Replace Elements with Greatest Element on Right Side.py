class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        mx = -1
        for i in xrange(-1, -len(arr) - 1, -1):
            arr[i], mx = mx, max(mx, arr[i])
        return arr
