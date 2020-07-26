class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        c = collections.Counter()
        for a2 in arr2:
            c[a2] = 0
        rem = []
        for a1 in arr1:
            if a1 in c:
                c[a1] += 1
            else:
                rem.append(a1)
        res = [None] * len(arr1)
        i = 0
        for a2 in arr2:
            for cnt in xrange(c[a2]):
                res[i] = a2
                i += 1
        res[i:] = sorted(rem)
        return res
