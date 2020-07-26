class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        if len(arr) <= 2:
            return True
        diff = arr[1] - arr[0]
        for i in xrange(len(arr) - 1):
            if diff != arr[i + 1] - arr[i]:
                return False
        return True
