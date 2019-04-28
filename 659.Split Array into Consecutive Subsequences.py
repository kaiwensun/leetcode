class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = collections.Counter(nums)
        for i in xrange(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            num = nums[i]
            helper = 0
            helper += min(counter[num - 1], counter[num - 2])
            helper += min(counter[num + 1], counter[num + 2])
            helper += max(0, min(counter[num - 1] - counter[num - 2], counter[num + 1] - counter[num + 2]))
            if helper < counter[num]:
                return False
        return True
