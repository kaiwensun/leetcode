class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        counter = collections.Counter(nums[:k + 1])
        if any(filter(lambda x: x > 1, counter.values())):
            return True
        for i in xrange(k + 1, len(nums)):
            counter[nums[i]] += 1
            counter[nums[i - k - 1]] -= 1
            if counter[nums[i]] == 2:
                return True
        return False
