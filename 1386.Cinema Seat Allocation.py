import collections
class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        cinema = collections.defaultdict(int)
        for seat in reservedSeats:
            cinema[seat[0]] |= 1 << seat[1] - 1
        res = 0
        for row in cinema.values():
            if row & 0b0111111110 == 0:
                res += 2
            elif row & 0b0001111000 == 0 or row & 0b0111100000 == 0 or row & 0b0000011110 == 0:
                res += 1
        return res + (n - len(cinema)) * 2
