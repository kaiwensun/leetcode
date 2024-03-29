class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        nums1, nums2 = nums[:len(nums) // 2], nums[len(nums) // 2:]
        sm1, sm2 = {0}, {0}
        for sm, nums in (sm1, nums1), (sm2, nums2):
            for num in nums:
                s = {old + num for old in sm}
                sm |= s
        sm2 = list(sorted(sm2))
        res = float("inf")
        for left in sm1:
            i = bisect.bisect_left(sm2, goal - left)
            for j in (i - 1, i):
                if 0 <= j < len(sm2):
                    res = min(res, abs(goal - (left + sm2[j])))
            if res == 0:
                break
        return res

