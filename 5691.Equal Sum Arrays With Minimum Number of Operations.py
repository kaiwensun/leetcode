from collections import Counter, defaultdict
class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort()
        nums2.sort()
        diff = sum(nums2) - sum(nums1)
        if diff < 0:
            diff = -diff
            nums1, nums2 = nums2, nums1
        res = 0
        i, j = 0, len(nums2) - 1
        while (i < len(nums1) or j >= 0) and diff > 0:
            diff1 = (6 - nums1[i]) if i < len(nums1) else 0
            diff2 = (nums2[j] - 1) if j >= 0 else 0
            if diff1 == diff2 == 0:
                break
            if diff1 > diff2:
                diff -= diff1
                i += 1
            else:
                diff -= diff2
                j -= 1
            res += 1
        return -1 if diff > 0 else res

