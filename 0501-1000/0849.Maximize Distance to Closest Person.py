class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        space = 1
        last = None
        for i, seat in enumerate(seats):
            if seat:
                if last is None:
                    space = i * 2
                else:
                    space = max(space, i - last)
                last = i
        space = max(space, (len(seats) - last - 1) * 2)
        return space // 2

