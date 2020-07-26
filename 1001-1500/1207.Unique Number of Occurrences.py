import collections
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter = collections.Counter(arr)
        cntOfCnt = collections.Counter(counter.values())
        return all(map(lambda cnt: cnt == 1, cntOfCnt.values()))
