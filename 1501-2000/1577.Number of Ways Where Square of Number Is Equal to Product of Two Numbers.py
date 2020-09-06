from collections import Counter
class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        keys1, keys2 = list(cnt1), list(cnt2)
        square1, square2 = Counter(num ** 2 for num in nums1), Counter(num ** 2 for num in nums2)
        res = 0
        for _ in xrange(2):
            for i in xrange(len(keys1)):
                for j in xrange(i, len(keys1)):
                    product = keys1[i] * keys1[j]
                    if product in square2:
                        pair = (cnt1[keys1[i]] - 1) * cnt1[keys1[i]] // 2 if i == j else cnt1[keys1[i]] * cnt1[keys1[j]]
                        res += pair * square2[product]
            keys1, keys2 = keys2, keys1
            cnt1, cnt2 = cnt2, cnt1
            square1, square2 = square2, square1
        return res

