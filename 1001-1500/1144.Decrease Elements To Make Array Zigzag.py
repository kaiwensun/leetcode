class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def cntMoves(decreasing):
            res = 0
            prev = nums[0]
            for i in xrange(1, len(nums)):
                if decreasing:
                    if prev <= nums[i]:
                        res += nums[i] - prev + 1
                        prev = prev - 1
                    else:
                        prev = nums[i]
                else:
                    if prev >= nums[i]:
                        res += prev - nums[i] + 1
                    prev = nums[i]
                decreasing = not decreasing
            return res
        return min(cntMoves(True), cntMoves(False))
