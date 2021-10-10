class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        nums = []
        for row in grid:
            nums.extend(row)
        if any((nums[i] - nums[i - 1]) % x for i in range(1, len(nums))):
            return -1
        nums.sort()
        medium = nums[len(nums) // 2]
        return sum(abs(num - medium) for num in nums) // x

