class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        mx = cnt = 0
        for i in xrange(len(light)):
            mx = max(mx, light[i])
            if mx == i + 1:
                cnt += 1
        return cnt
