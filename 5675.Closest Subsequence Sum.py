class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        nums1, nums2 = nums[:len(nums) // 2], nums[len(nums) // 2:]
        sm1, sm2 = {0}, {0}
        for num in nums1:
            s = set()
            for old in sm1:
                s.add(old + num)
            sm1 |= s
        for num in nums2:
            s = set()
            for old in sm2:
                s.add(old + num)
            sm2 |= s
        sm2 = list(sorted(sm2))
        res = float("inf")
        for left in sm1:
            i = bisect.bisect_left(sm2, goal - left)
            for j in (i - 1, i, i + 1):
                if 0 <= j < len(sm2):
                    res = min(res, abs(goal - (left + sm2[j])))
        return res

