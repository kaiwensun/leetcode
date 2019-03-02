class Cell(object):
    def __init__(self, prev_k_sum, max_sum1, index1, max_sum2, index2, max_sum3, index3):
        self.prev_k_sum = prev_k_sum
        self.max_sum1 = max_sum1
        self.index1 = index1
        self.max_sum2 = max_sum2
        self.index2 = index2
        self.max_sum3 = max_sum3
        self.index3 = index3
        
    def __str__(self):
        return "prev_k_sum: {}, max1: ({}, {}), max2: ({}, {}), max3: ({}, {})".format(self.prev_k_sum, self.max_sum1, self.index1, self.max_sum2, self.index2, self.max_sum3, self.index3)
        
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """
        DP contains:
        - prev_k_sum
        - (max_sum_1, index): the max sum of 1 interval, and its ending index
        - (max_sum_2, index): the max sum of 2 intervals, and its ending index
        - (max_sum_3, index): the max sum of 3 intervals, and its ending index
        """
        _DP = [Cell(float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf')) for _ in xrange(len(nums))]
        _overflow = Cell(0, float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf'))
        def assignMax(val1, ind1, val2, ind2):
            return (val2, ind2) if val1 < val2 else (val1, ind1)
        def DP(i):
            if i < 0:
                return _overflow
            return _DP[i]
        def getNums(i):
            return 0 if i < 0 else nums[i]
        def constructResult():
            result = [0] * 3
            result[2] = DP(len(nums) - 1).index3 - k + 1
            result[1] = DP(result[2] - 1).index2 - k + 1
            result[0] = DP(result[1] - 1).index1 - k + 1
            return result

        for i in xrange(len(nums)):
            DP(i).prev_k_sum = DP(i - 1).prev_k_sum + getNums(i)
            DP(i).prev_k_sum -= getNums(i - k)
            DP(i).max_sum1, DP(i).index1 = assignMax(DP(i - 1).max_sum1, DP(i - 1).index1, DP(i).prev_k_sum, i)
            DP(i).max_sum2, DP(i).index2 = assignMax(DP(i - 1).max_sum2, DP(i - 1).index2, DP(i - k).max_sum1 + DP(i).prev_k_sum, i)
            DP(i).max_sum3, DP(i).index3 = assignMax(DP(i - 1).max_sum3, DP(i - 1).index3, DP(i - k).max_sum2 + DP(i).prev_k_sum, i)
        return constructResult()
