class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        res = [[None] * c for _ in xrange(r)]
        i = j = 0
        for row in nums:
            for num in row:
                res[i][j] = num
                j += 1
                if j == c:
                    j = 0
                    i += 1
        return res
