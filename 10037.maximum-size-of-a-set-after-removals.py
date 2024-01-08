class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1) // 2
        s1 = set(nums1)
        s2 = set(nums2)
        d1 = s1 - s2
        d2 = s2 - s1
        joint = s1 & s2
        sz1 = min(n, len(d1))
        sz2 = min(n, len(d2))
        return min(2 * n, sz1 + sz2 + len(joint))

