class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        mn = min(nums)
        mx = max(nums)
        interval = (mx - mn + len(nums) - 2) / (len(nums) - 1)
        if interval == 0:
            return 0
        buckets = [[float("inf"), float("-inf")] for _ in xrange(mn, mx + 1, interval)]
        for num in nums:
            index = (num - mn) // interval
            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)
        last = float("inf")
        res = 0
        for bucket in buckets:
            if bucket[0] > mx:
                continue
            res = max(res, bucket[0] - last)
            last = bucket[1]
        return res

