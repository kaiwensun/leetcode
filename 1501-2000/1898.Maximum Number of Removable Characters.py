class Solution(object):
    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """
        def test(k):
            k_removables = set(removable[:k])
            j = 0
            for i in xrange(len(s)):
                if i in k_removables:
                    continue
                if s[i] == p[j]:
                    j += 1
                    if j == len(p):
                        return True
            return False

        l, r = 1, len(removable) + 1
        while l < r:
            mid = (l + r) // 2
            if test(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1

