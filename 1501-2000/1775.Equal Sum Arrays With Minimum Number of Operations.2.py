from collections import Counter, defaultdict
class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        diff = sum(nums2) - sum(nums1)
        if diff < 0:
            diff = -diff
            nums1, nums2 = nums2, nums1
        cnt1, cnt2 = Counter(nums1), Counter(nums2)    
        res = 0
        i, j = min(cnt1.keys()), max(cnt2.keys())
        while (i <= 6 or j >= 1) and diff > 0:
            while i <= 6 and i not in cnt1:
                i += 1
            while j >= 1 and j not in cnt2:
                j -= 1
            diff1 = 6 - i
            diff2 = j - 1
            if diff1 <= 0 >= diff2:
                break
            if diff1 > diff2:
                res += min(cnt1[i], (diff + diff1 - 1) // diff1)
                diff -= diff1 * cnt1[i]
                i += 1
            else:
                res += min(cnt2[j], (diff + diff2 - 1) // diff2)
                diff -= diff2 * cnt2[j]
                j -= 1
        return -1 if diff > 0 else res

