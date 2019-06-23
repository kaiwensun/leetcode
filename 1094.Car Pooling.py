class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        drop = collections.Counter()
        pick = collections.Counter()
        for trip in trips:
            pick[trip[1]] += trip[0]
            drop[trip[2]] += trip[0]
        drop = list(sorted(drop.iteritems()))
        pick = list(sorted(pick.iteritems()))
        dp = pp = 0
        while dp < len(drop) and pp < len(pick):
            d = drop[dp] if dp < len(drop) else (float('inf'), 0)
            p = pick[pp] if pp < len(pick) else (float('inf'), 0)
            if d[0] <= p[0]:
                capacity += d[1]
                dp += 1
            else:
                capacity -= p[1]
                pp += 1
                if capacity < 0:
                    return False
        return True
