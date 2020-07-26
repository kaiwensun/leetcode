from collections import Counter
class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        rval = 0
        M = 10 ** 9 + 7
        two_sum_count = Counter()
        element_count = Counter()
        for a in A[::-1]:
            two_sum = target - a
            rval = (rval + two_sum_count[two_sum]) % M
            for k, v in element_count.items():
                two_sum_count[a + k] = (two_sum_count[a + k] + v) % M
            element_count[a] = (element_count[a] + 1) % M
        return rval
