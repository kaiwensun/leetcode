class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        res = 0
        left, right, width = 0, len(text), 1
        while left < len(text) / 2:
            for width in xrange(1, len(text) / 2 - left + 1):
                # print text[left: left + width] == text[right - width: right], text[left: left + width], text[right - width: right]
                if text[left: left + width] == text[right - width: right]:
                    # print text[left: left + width] 
                    left = left + width
                    right = right - width
                    res += 2
                    break
            else:
                res += 1
                break
        else:
            if left + 1 == right:
                res += 1
        return res
