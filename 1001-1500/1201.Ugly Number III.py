from fractions import gcd
class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def lcm(a, b):
            return max(a, b) / gcd(a, b) * min(a, b)
        
        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(a, bc)
        factors = (a, b, c, ab, bc, ac, abc)
        
        def get_count(num):
            counts = map(num.__div__, factors)
            return sum(counts) - 2 * sum(counts[3:6])

        l, r = 0, 2 * 10**9 + 1
        while l + 1 < r:
            mid = l + (r - l) / 2
            cnt = get_count(mid)
            if cnt == n:
                if r == mid + 1:
                    return l if get_count(l) == n else mid
                r = mid + 1
            elif cnt < n:
                l = mid + 1
            else:
                r = mid
        return l
