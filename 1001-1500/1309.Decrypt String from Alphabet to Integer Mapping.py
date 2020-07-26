class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        i = 0
        def toLetter(n):
            return chr(ord('a') + int(n) - 1)
        def nextToken(i):
            if i + 2 < len(s) and s[i + 2] == "#":
                return toLetter(s[i : i + 2]), i + 3
            else:
                return toLetter(s[i]), i + 1
        while i < len(s):
            token, i = nextToken(i)
            res.append(token)
        return "".join(res)
