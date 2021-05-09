class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        sorted_nums2 = [(num, index) for index, num in enumerate(nums2)]
        sorted_nums2.sort()
        res = 0
        for i in range(len(nums1)):
            while sorted_nums2 and nums1[i] <= sorted_nums2[-1][0]:
                if i <= sorted_nums2[-1][1]:
                    res = max(res, sorted_nums2[-1][1] - i)
                sorted_nums2.pop()
        return res

