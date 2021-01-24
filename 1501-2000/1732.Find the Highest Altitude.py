class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        return reduce(lambda acc, g: (acc[0] + g, max(acc[1], acc[0] + g)), gain, (0, 0))[1]

