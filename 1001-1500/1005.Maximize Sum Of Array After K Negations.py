class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        neg = [x for x in A if x < 0 ]
        zeros = [x for x in A if x == 0 ]
        pos = [x for x in A if x > 0]
        if K <= len(neg):
            neg.sort()
            for i in xrange(K):
                neg[i] = -neg[i]
            return sum(neg) + sum(pos)
        elif K <= len(neg) + len(zeros):
            return -sum(neg) + sum(pos)
        else:
            if len(zeros):
                return -sum(neg) + sum(pos)
            else:
                k = (K - len(neg)) % 2
                if k:
                    a = sorted([abs(x) for x in A])
                    a[0] = -a[0]
                    return sum(a)
                else:
                    return -sum(neg) + sum(pos)
                
          
