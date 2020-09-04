class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left, right = {}, {}
        for i, c in enumerate(S):
            left.setdefault(c, i)
            right[c] = i
        res = []
        l, r = -1, 0
        for i, c in enumerate(S):
            r = max(r, right[c])
            if i == r:
                res.append(r - l)
                l = i
        return res

