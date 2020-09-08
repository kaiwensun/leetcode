import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        size = len(nums)
        nums_index = [[(n, g) for n in nums[g]] for g in xrange(len(nums))]
        nums_index = list(heapq.merge(*nums_index))
        l = r = 0
        counter = {}
        result = [0, nums_index[-1][0]]
        while r <= len(nums_index) and l < len(nums_index):
            if len(counter) < size and r < len(nums_index):
                n, g = nums_index[r]
                counter.setdefault(g, 0)
                counter[g] += 1
                r += 1
            else:
                n, g = nums_index[l]
                counter[g] -= 1
                if counter[g] == 0:
                    del counter[g]
                l += 1
            if len(counter) == size:
                if nums_index[r - 1][0] - nums_index[l][0] < result[1] - result[0]:
                    result = [nums_index[l][0], nums_index[r - 1][0]]
        return result

