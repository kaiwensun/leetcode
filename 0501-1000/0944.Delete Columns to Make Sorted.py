class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # result = 0
        # for col in xrange(len(A[0])):
        #     for row in xrange(len(A) - 1):
        #         if A[row][col] > A[row + 1][col]:
        #             result += 1
        #             break
        # return result
        return len([s for s in zip(*A) if list(s) != sorted(s)])
