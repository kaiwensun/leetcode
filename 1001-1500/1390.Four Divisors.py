import collections, math
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted(nums)
        cnt = [0] * len(nums)
        sm = [0] * len(nums)
        sq = math.sqrt(nums[-1])
        smallest_index = 0
        for div in xrange(1, int(sq) + 1):
            for i in xrange(smallest_index, len(nums)):
                num = nums[i]
                if num % div == 0:
                    div_res = num // div
                    if div < div_res:
                        cnt[i] += 2
                        sm[i] += div + div_res
                    elif div == div_res:
                        cnt[i] += 1
                        sm[i] += div
                        smallest_index = i + 1
                    else:
                        smallest_index = i + 1
        res = 0
        for i in xrange(len(nums)):
            if cnt[i] == 4:
                res += sm[i]
        return res
