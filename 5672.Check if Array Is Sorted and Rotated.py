class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mn = min(nums)
        mx = max(nums)
        if mn == mx:
            return True
        if nums[-1] == mn:
            for start in xrange(- 1, -len(nums) -1, -1):
                if nums[start] != mn:
                    start += 1
                    break
        else:
            start = nums.index(mn)
        if start >= 0:
            start -= len(nums)
        for i in xrange(start, start + len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True

