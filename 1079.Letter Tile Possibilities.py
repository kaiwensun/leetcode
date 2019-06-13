class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        def helper(counter):
            res = 0
            for k, v in counter.items():
                if v > 0:
                    counter[k] -= 1
                    res += 1 + helper(counter)
                    counter[k] += 1
            return res
        counter = collections.Counter(tiles)
        return helper(counter)
