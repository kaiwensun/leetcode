class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        total = reduce(lambda xor, i: xor ^ i, xrange(1, len(encoded) + 2))
        a1 = reduce(lambda remain, i: remain ^ i, encoded[1::2], total)
        res = [a1]
        for num in encoded:
            res.append(res[-1] ^ num)
        return res

