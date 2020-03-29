# https://www.zhihu.com/question/21923021
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def calcMaxMatchLen(needle):
            res = [0] * len(needle)
            maxLen = 0
            for i in xrange(1, len(needle)):
                while maxLen and needle[maxLen] != needle[i]:
                    maxLen = res[maxLen - 1]
                if needle[maxLen] == needle[i]:
                    maxLen += 1
                res[i] = maxLen
            return res
        if not needle:
            return 0
        maxMatchLen = calcMaxMatchLen(needle)
        needle_ind = 0
        for i in xrange(len(haystack)):
            while needle_ind and haystack[i] != needle[needle_ind]:
                needle_ind = maxMatchLen[needle_ind - 1]
            if haystack[i] == needle[needle_ind]:
                needle_ind += 1
            if needle_ind == len(needle):
                return i - len(needle) + 1
        return -1
