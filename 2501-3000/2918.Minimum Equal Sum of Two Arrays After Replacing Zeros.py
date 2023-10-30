class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sm1, sm2 = sum(nums1), sum(nums2)
        ones1, ones2 = nums1.count(0), nums2.count(0)
        if ones1 == 0 and sm1 < sm2 + ones2:
            return -1
        if ones2 == 0 and sm2 < sm1 + ones1:
            return -1
        return max(sm1 + ones1, sm2 + ones2)

