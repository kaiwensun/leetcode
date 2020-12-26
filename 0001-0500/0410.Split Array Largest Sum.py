import bisect
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        prefix = list(nums)
        for i in xrange(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        def test(sm):
            index = 0
            target = sm
            for i in xrange(m):
                new_index = bisect.bisect_right(prefix, target, index, len(prefix))
                if new_index == index:
                    return False
                if new_index == len(prefix):
                    return True
                target = prefix[new_index - 1] + sm
                index = new_index
            return False

        l, r = min(nums), sum(nums) + 1
        while l < r:
            mid = (l + r) // 2
            if test(mid):
                r = mid
            else:
                l = mid + 1
        return l

