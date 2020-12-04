class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def slope(i):
            left = arr[i - 1] if i else float("-inf")
            right = arr[i + 1] if i != len(arr) - 1 else float("-inf")
            if left < arr[i] < right:
                return -1
            elif left < arr[i] > right:
                return 0
            elif left > arr[i] > right:
                return 1
            else:
                assert(False)
        
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            s = slope(mid)
            if s == 0:
                return mid
            elif s == -1:
                l = mid + 1
            else:
                r = mid
        assert(False)

