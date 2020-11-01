from collections import Counter
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for v, times in sorted(Counter(nums).iteritems(), key=lambda (v, times) : (times, -v)):
            res.extend([v] * times)
        return res

