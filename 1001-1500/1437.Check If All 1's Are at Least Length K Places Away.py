class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last = -k - 1
        for i, num in enumerate(nums):
            if num == 1:
                if i - last > k:
                    last = i
                else:
                    return False
        return True
