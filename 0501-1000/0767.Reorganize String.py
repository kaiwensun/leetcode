from collections import Counter
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = [None] * len(S)
        i = 0
        for c, t in Counter(S).most_common():
            for _ in range(t):
                if (i != 0 and res[i - 1] == c) or (i != len(S) - 1 and res[i + 1] == c):
                    return ""
                res[i] = c
                i += 2
                if i >= len(S):
                    i = 1
        return "".join(res)

