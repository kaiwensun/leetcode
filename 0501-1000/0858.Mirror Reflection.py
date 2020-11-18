from fractions import gcd
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        g = gcd(p, q)
        x = p // g
        y = q // g
        return (~x & 1) << 1 or y & 1

