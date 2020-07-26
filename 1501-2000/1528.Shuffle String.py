class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = [None] * len(s)
        for i, target in enumerate(indices):
            res[target] = s[i]
        return "".join(res)