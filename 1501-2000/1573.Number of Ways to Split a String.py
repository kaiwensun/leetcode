from collections import Counter
class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = Counter(s)["1"]
        if total % 3 != 0:
            return 0
        if total == 0:
            return ((len(s) - 1) * (len(s) - 2) // 2)  % (10 ** 9 + 7)
        split = total // 3
        buffers = []
        buf = ones = 0
        for i, c in enumerate(s):
            if c == "1":
                if ones == split:
                    buffers.append(buf)
                    buf = ones = 0
                ones += 1
            elif ones == split:
                buf += 1
        return ((buffers[0] + 1) * (buffers[1] + 1)) % (10 ** 9 + 7)

