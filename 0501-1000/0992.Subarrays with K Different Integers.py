class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        def atMostK(K):
            res = 0
            start = 0
            counter = collections.Counter()
            for end in xrange(len(A)):
                if counter[A[end]] == 0:
                    K -= 1
                counter[A[end]] += 1
                while K < 0:
                    counter[A[start]] -= 1
                    if counter[A[start]] == 0:
                        K += 1
                    start += 1
                res += end - start + 1
            return res
        return atMostK(K) - atMostK(K - 1)
