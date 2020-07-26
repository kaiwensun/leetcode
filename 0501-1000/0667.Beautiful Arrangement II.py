class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = [None] * n
        odd = k % 2
        res[1 - odd:k - odd:2], res[odd:k:2], res[k - odd:] = range(1, k / 2 + 1), range(n, n - k / 2, - 1), range(k / 2 + 1, n - k / 2 + 1)
        return res
