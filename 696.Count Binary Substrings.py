class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        prevCnt = 0
        currCnt = 0
        prevNum = None
        for c in s:
            if prevNum is None:
                currCnt += 1
            else:
                if prevNum == c:
                    currCnt += 1
                    if currCnt <= prevCnt:
                        res += 1
                else:
                    prevCnt, currCnt = currCnt, 1
                    res += 1
            prevNum = c
        return res
