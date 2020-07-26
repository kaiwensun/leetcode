from collections import Counter
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        cnt = Counter(arr)
        for i, num in enumerate(sorted(cnt.values())):
            k -= num
            if k <= 0:
                return len(cnt) - i - 1 if k == 0 else len(cnt) - i
        return 0
