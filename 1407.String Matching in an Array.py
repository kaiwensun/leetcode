class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for w1 in words:
            for w2 in words:
                if w1 != w2 and w1 in w2:
                    res.append(w1)
                    break
        return res
