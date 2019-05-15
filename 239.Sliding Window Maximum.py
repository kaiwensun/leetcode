class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        candidates = collections.deque()
        res = [None] * (len(nums) - k + 1)
        for i, n in enumerate(nums):
            while candidates and candidates[-1][0] <= n:
                candidates.pop()
            while candidates and i - candidates[0][1] + 1 > k:
                candidates.popleft()
            candidates.append((n, i))
            if i >= k - 1:
                res[i + 1 - k] = candidates[0][0]
        return res
