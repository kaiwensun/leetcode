class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        res = []
        text = text.split()
        for i in xrange(len(text) - 2):
            if first == text[i] and second == text[i + 1]:
                res.append(text[i + 2])
        return res
