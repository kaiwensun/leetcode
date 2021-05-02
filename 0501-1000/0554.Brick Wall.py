from collections import Counter

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        cnt = Counter()
        for row in wall:
            length = 0
            for brik in row:
                length += brik
                cnt[length] += 1
        cnt[length] = 0
        return len(wall) - max(cnt.values())

