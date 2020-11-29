import collections, bisect

class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        sorted_max = list(sorted(max(nums[i], nums[-i - 1]) for i in xrange(len(nums) // 2)))
        sorted_min = list(sorted(min(nums[i], nums[-i - 1]) for i in xrange(len(nums) // 2)))
        cnt = collections.Counter(nums[i] + nums[-i - 1] for i in xrange(len(nums) // 2))
        res = len(nums)
        for common in xrange(2, limit * 2 + 1):
            change_two_1 = bisect.bisect_left(sorted_max, common - limit)
            change_two_2 = len(sorted_max) - bisect.bisect_left(sorted_min, common)
            change_zero = cnt[common]
            change_two = change_two_1 + change_two_2
            change_one = len(sorted_max) - change_zero - change_two
            res = min(res, change_two * 2 + change_one)
        return res

