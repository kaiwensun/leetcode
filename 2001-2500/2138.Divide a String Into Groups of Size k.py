class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        res = []
        for start in range(0, len(s), k):
            end = start + k
            if end > len(s):
                res.append(s[start:end] + fill * (end - len(s)))
            else:
                res.append(s[start: end])
        return res

