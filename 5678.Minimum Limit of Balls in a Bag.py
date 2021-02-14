class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def can_split(size):
            res = 0
            for num in nums:
                res += (num - 1) // size
                if res > maxOperations:
                    return False
            return True

        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            if can_split(mid):
                r = mid
            else:
                l = mid + 1
        return l

