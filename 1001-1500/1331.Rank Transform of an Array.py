class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr = sorted((v, i) for i, v in enumerate(arr))
        rank = 0
        res = [None] * len(arr)
        for i in xrange(len(arr)):
            if i == 0 or arr[i - 1][0] != arr[i][0]:
                rank += 1
            res[arr[i][1]] = rank
        return res
