class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        res = [first]
        for item in encoded:
            res.append(res[-1] ^ item)
        return res

