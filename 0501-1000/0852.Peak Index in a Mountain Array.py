class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def slope(i):
            left = arr[i - 1]
            right = arr[i + 1]
            if left < arr[i] < right:
                return -1
            elif left < arr[i] > right:
                return 0
            elif left > arr[i] > right:
                return 1
            else:
                assert(False)
        
        l, r = 0, len(arr)
        arr.append(float("-inf"))
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

