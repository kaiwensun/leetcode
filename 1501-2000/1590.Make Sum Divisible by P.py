class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        residual = sum(nums) % p
        if residual == 0:
            return 0
        sm, res = 0, float("inf")
        sm2index = {0: -1}
        for i, num in enumerate(nums):
            sm = (sm + num) % p
            res = min(res, i - sm2index.get((sm - residual) % p, float("-inf")))
            sm2index[sm] = i
        return -1 if res in (float('inf'), len(nums)) else res

