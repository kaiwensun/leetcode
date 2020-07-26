class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        Bc = collections.Counter()
        for b in B:
            bc = collections.Counter(b)
            for k, v in bc.iteritems():
                Bc[k] = max(Bc[k], v)
        res = []
        for a in A:
            ac = collections.Counter(a)
            for k, v in Bc.iteritems():
                if ac[k] < v:
                    break
            else:
                res.append(a)
        return res
