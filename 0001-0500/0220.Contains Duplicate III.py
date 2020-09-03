class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 or k <= 0:
            return False
        seen = {}
        width = t + 1
        for i, num in enumerate(nums):
            bucket = num // width
            if bucket in seen:
                return True
            for drift in [-1, 1]:
                if bucket + drift in seen and abs(seen[bucket + drift] - num) <= t:
                    return True
            if i >= k:
                del seen[nums[i - k] // width]
            seen[bucket] = num
        return False

