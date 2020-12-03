import bisect
class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def longest_increasing_subsequence(nums):
            height_stack = [float("-inf")]
            length_stack = [0]
            res = []
            for index, num in enumerate(nums):
                posi = bisect.bisect_left(height_stack, num)
                length = length_stack[posi - 1] + 1
                res.append(length)
                if posi == len(height_stack):
                    height_stack.append(num)
                    length_stack.append(length)
                else:
                    height_stack[posi] = num
                    length_stack[posi] = length
            return res

        left_lis_sizes = longest_increasing_subsequence(nums)
        right_lis_sizes = list(reversed(longest_increasing_subsequence(reversed(nums))))

        # mountain peak cannot be at the very end of the mountain
        for i in xrange(len(left_lis_sizes)):
            if left_lis_sizes[i] != 1:
                break
            left_lis_sizes[i] = float("-inf")
        for i in xrange(len(right_lis_sizes) - 1, -1, -1):
            if right_lis_sizes[i] != 1:
                break
            right_lis_sizes[i] = float("-inf")
        return len(nums) - max(a + b for a, b in zip(left_lis_sizes, right_lis_sizes)) + 1

