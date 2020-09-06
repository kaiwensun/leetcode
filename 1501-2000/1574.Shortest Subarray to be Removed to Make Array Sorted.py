class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def isSorted(start, end):
            num = float("-inf")
            for i in xrange(start, end):
                if num > arr[i]:
                    return False
                num = arr[i]
            return True
        arr = [float("-inf")] + arr + [float("inf")]
        num = float("-inf")
        for i in xrange(len(arr)):
            if num > arr[i]:
                first_drop = i
                break
            num = arr[i]
        else:
            return 0
        res = len(arr) - first_drop
        res = min(res, first_drop if isSorted(first_drop, len(arr)) else float("inf"))
        l, r = first_drop - 1, len(arr) - 1
        while l >= 0 and arr[l] > arr[r]:
            l -= 1
        while l >= 0:
            while arr[l] <= arr[r - 1] <= arr[r]:
                r -= 1
            res = min(res, r - l - 1)
            l -= 1
        return res

