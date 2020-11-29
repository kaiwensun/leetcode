import heapq
from collections import deque
class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            if nums[i] & 1:
                nums[i] <<= 1
        nums = [-x for x in nums]
        heapq.heapify(nums)
        mn, mx = -max(nums), -nums[0]
        diff = mx - mn
        while nums[0] & 1 == 0:
            mn = min(mn, (-nums[0]) >> 1)
            heapq.heappushpop(nums, -((-nums[0]) >> 1))
            mx = min(mx, -nums[0])
            diff = min(diff, mx - mn)
        return diff

