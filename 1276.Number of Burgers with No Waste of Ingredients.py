class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        j = (tomatoSlices - cheeseSlices * 2)
        if j %2 != 0:
            return []
        j /= 2
        s = cheeseSlices - j
        if j >= 0 and s >= 0:
            return [j, s]
        return []
