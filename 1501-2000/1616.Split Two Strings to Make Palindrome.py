class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        def middlePalindromeSize(s):
            r = len(s) // 2
            l = r - 1 + len(s) % 2
            while r < len(s) and s[r] == s[l]:
                l -= 1
                r += 1
            return r - l - 1
        
        middleSize = max(middlePalindromeSize(a), middlePalindromeSize(b))
        l, r = 0, len(b) - 1
        while l <= r and a[l] == b[r]:
            l += 1
            r -= 1
        
        if r - l + 1 <= middleSize:
            return True
        l, r = 0, len(a) - 1
        while l <= r and b[l] == a[r]:
            l += 1
            r -= 1
        if r - l + 1 <= middleSize:
            return True
        return False

