from collections import deque

MOD = 10 ** 9 + 7
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:

        queue = deque([(0, 0)])  # (num, prefix_sum)
        res = 0
        nums.append(-1)
        for num in nums:
            prefix_sum = 0
            while queue and queue[-1][0] >= num:
                prefix_sum += queue[-1][1]
                res = max(res, queue[-1][0] * prefix_sum)
                queue.pop()
            prefix_sum += num
            queue.append((num, prefix_sum))
        return res % MOD

