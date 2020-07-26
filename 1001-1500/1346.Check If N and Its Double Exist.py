import collections
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s = collections.Counter(arr)
        if s[0] >= 2:
            return True
        del s[0]
        for n in arr:
            if n * 2 in s:
                return True
        return False
