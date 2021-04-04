class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sorted1 = list(sorted(nums1))
        res = sum(abs(num1 - num2) for num1, num2 in zip(nums1, nums2))
        diff = 0
        for i in range(len(nums1)):
            j = bisect.bisect_right(sorted1, nums2[i])
            for k in j - 1, j:
                if 0 <= k < len(nums1):
                    diff = min(diff, abs(nums2[i] - sorted1[k]) - abs(nums2[i] - nums1[i]))
        return (res + diff) % (10 ** 9 + 7)

