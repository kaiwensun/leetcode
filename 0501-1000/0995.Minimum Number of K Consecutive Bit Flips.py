class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        length = len(A)
        ones = sum(A)
        zeros = length - ones
        if zeros == 0:
            return 0
        cnt = 0
        i = 0
        while i < length:
            if A[i] == 0:
                if length - i < K:
                    return -1
                end = None
                for j in range(i + 1, i + K):
                    if A[j] == 1:
                        end = j
                        break
                if end is None:
                    # flip A[i: K]
                    i = i + K - 1
                    cnt += 1
                else:
                    if length - end < K:
                        return -1
                    A[i + K: end + K] = [1 - a for a in A[i + K: end + K]]
                    i = end  - 1
                    cnt += 2

            i += 1
        return cnt
