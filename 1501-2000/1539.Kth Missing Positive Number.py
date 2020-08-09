class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            num = arr[mid]
            if num - 1 - mid < k:
                l = mid + 1
            else:
                r = mid
        return k + l  # arr[l - 1] + k - (arr[l - 1] - l)
