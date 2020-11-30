import bisect
class Solution(object):
    def breakfastNumber(self, staple, drinks, x):
        """
        :type staple: List[int]
        :type drinks: List[int]
        :type x: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        drinks.sort()
        res = 0
        for s in sorted(staple):
            res += bisect.bisect_right(drinks, x - s)
            res %= MOD
        return res 

