class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return [0] * len(code)
        sm = sum(code[1 : k + 1]) if k > 0 else sum(code[k:])
        res = [0] * len(code)
        l, r = min(k - 1, 0), max(k, -1)
        for i in xrange(0, len(code),):
            res[i] = sm
            l += 1
            r += 1
            sm += code[r % len(code)] - code[l % len(code)]
        return res

