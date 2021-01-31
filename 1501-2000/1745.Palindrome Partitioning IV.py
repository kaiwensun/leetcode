class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        extend_to = [set() for _ in xrange(len(s))]
        for i in xrange(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                extend_to[l].add(r + 1)
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                extend_to[l].add(r + 1)
                l -= 1
                r += 1
        for i1 in extend_to[0]:
            for i2 in extend_to[i1]:
                if len(s) in extend_to[i2]:
                    return True
        return False

