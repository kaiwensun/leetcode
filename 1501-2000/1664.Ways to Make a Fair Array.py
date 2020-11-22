class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0, 0]
        for num in nums:
            prefix.append(prefix[-2] + num)

        def get_range_sum(start, end):
            if end & 1 != start & 1:
                end -= 1
            if start > end:
                return 0
            return prefix[end + 2] - prefix[start]
        res = 0
        for i in xrange(0, len(nums)):
            odd_sum = get_range_sum(1, i - 1) + get_range_sum(i + 2 - i % 2, len(nums) - 1)
            even_sum = get_range_sum(0, i - 1) + get_range_sum(i + 1 + i % 2, len(nums) - 1)
            res += int(odd_sum == even_sum)
        return res

