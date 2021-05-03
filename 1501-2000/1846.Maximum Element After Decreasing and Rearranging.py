class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        arr.append(0)
        for i in range(len(arr) - 1):
            arr[i] = min(arr[i], arr[i - 1] + 1)
        return arr[-2]

