class Solution(object):
    def getRow(self, k):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # C_k_i = k! / (i! * (k - i)!)
        f = [1] * (k + 1)
        for i in xrange(1, k + 1):
            f[i] = f[i - 1] * i
        res = [None] * (k + 1)
        for i in xrange(k + 1):
            res[i] = f[k] // f[i] // f[k - i]
        return res
