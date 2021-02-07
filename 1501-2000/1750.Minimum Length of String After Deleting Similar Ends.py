class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            c = s[l]
            while l < len(s) and s[l] == c:
                l += 1
            if l > r:
                break
            while s[r] == c:
                r -= 1
        return r - l + 1

