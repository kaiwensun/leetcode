class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        res = [None] * len(seq)
        A = B = 0
        for i, c in enumerate(seq):
            if c == '(':
                if A <= B:
                    A += 1
                    res[i] = 0
                else:
                    B += 1
                    res[i] = 1
            else:
                if A >= B:
                    A -= 1
                    res[i] = 0
                else:
                    B -= 1
                    res[i] = 1
        return res
