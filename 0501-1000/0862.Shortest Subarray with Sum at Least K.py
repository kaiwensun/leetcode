from collections import deque
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = float("inf")
        prefix_sum = [0] * (len(A) + 1)
        for i in xrange(len(A)):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]
        queue = deque()
        for i, num in enumerate(prefix_sum):
            while queue and queue[0][1] <= num - K:
                res = min(res, i - queue.popleft()[0])
            while queue and queue[-1][1] >= num:
                queue.pop()
            queue.append((i, num))
        return res if res != float("inf") else -1

