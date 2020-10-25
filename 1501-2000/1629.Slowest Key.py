class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        mx = (releaseTimes[0], keysPressed[0])
        for i in xrange(1, len(releaseTimes)):
            mx = max(mx, (releaseTimes[i] - releaseTimes[i - 1], keysPressed[i]))
        return mx[1]

