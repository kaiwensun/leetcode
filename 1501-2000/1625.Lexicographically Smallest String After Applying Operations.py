from fractions import gcd
class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        def get_smallest_head(head, a):
            if a == 5:
                return min(head, (head + 5) % 10)
            return 0 if a % 2 else head % 2
            
        def add_a(lst, diff_odd, diff_even):
            for i in xrange(1, len(lst), 2):
                lst[i] += diff_odd
                lst[i] %= 10
            if diff_even:
                for i in xrange(0, len(lst), 2):
                    lst[i] += diff_even
                    lst[i] %= 10
            return lst
            
        res = list(map(int, s))
        cur = list(map(int, s))
        rotate_times = len(s) // gcd(b, len(s))
        for _ in xrange(rotate_times):
            diff_odd = get_smallest_head(cur[1], a) - cur[1]
            diff_even = b % 2 and get_smallest_head(cur[0], a) - cur[0]
            if res > add_a(cur, diff_odd, diff_even):
                res = list(cur)
            cur = cur[b:] + cur[:b]
        return "".join(map(str, res))

