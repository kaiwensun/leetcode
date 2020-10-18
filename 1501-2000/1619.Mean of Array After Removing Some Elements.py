from collections import Counter
class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        size = len(arr) // 20
        print(list(sorted(arr))[size:-size-1])
        return sum(list(sorted(arr))[size:-size]) / (len(arr) * 0.9)

