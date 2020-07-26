class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        size = (len(arr)) / 4
        # accept should > size
        mx = max(1, size)
        for index in range(0, len(arr), mx):
            candidate = arr[index]
            left = bisect.bisect_left(arr, candidate, max(0, index - mx), min(len(arr), index + mx))
            right = bisect.bisect_right(arr, candidate, max(0, index - mx), min(len(arr), index + mx))
            if right - left > size:
                return arr[index]
        assert(False)
