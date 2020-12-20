class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = r = 0
        res = 0
        seen = set()
        sm = 0
        for r in xrange(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
                sm -= nums[l]
                l += 1
            seen.add(nums[r])
            sm += nums[r]
            res = max(res, sm)
        return res

