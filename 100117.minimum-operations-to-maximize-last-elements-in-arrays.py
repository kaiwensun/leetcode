class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[-1] > nums2[-1]:
            nums1, nums2 = nums2, nums1
        res1 = 0
        for num1, num2 in zip(nums1[:-1], nums2[:-1]):
            if num1 > nums1[-1] or num2 > nums2[-1]:
                if num2 <= nums1[-1] and num1 <= nums2[-1]:
                    res1 += 1
                else:
                    res1 = float("inf")
                    break
        res2 = 1
        for num1, num2 in zip(nums1[:-1], nums2[:-1]):
            if num2 > nums1[-1] or num1 > nums2[-1]:
                if num2 <= nums2[-1] and num1 <= nums1[-1]:
                    res2 += 1
                else:
                    res2 = float("inf")
                    break
        res = min(res1, res2)
        return -1 if res == float("inf") else res

