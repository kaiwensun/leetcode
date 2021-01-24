class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        volume = 0
        edge = 1
        diff = 1
        while volume + diff <= n:
            volume += diff
            edge += 1
            diff = (edge + 1) * edge // 2
        edge -= 1
        res = (edge + 1) * edge // 2
        diff = n - volume
        for consumed in xrange(1, edge + 2):
            if diff <= 0:
                break
            res += 1
            diff -= consumed
        return res

