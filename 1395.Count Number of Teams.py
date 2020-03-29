from bisect import bisect
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        cnt_l = [0] * len(rating)
        cnt_r = [0] * len(rating)
        arr = []
        for i in xrange(len(rating)):
            posi = bisect(arr, rating[i])
            cnt_l[i] = posi
            arr.insert(posi, rating[i])
        arr = []
        for i in xrange(len(rating) - 1, -1 , -1):
            posi = bisect(arr, rating[i])
            cnt_r[i] = posi
            arr.insert(posi, rating[i])
        res = 0
        for i in xrange(n):
            res += cnt_l[i] * (n - i - 1 - cnt_r[i]) + cnt_r[i] * (i - cnt_l[i])
        return res
