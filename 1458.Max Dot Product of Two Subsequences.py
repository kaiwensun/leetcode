from functools import lru_cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
	
        # Max prefixes are actually not necessary.
	# They are just a small optimization that doesn't significantly affect time complexity.
        maxPrefix1 = [nums1[0]] * len(nums1)
        maxPrefix2 = [nums2[0]] * len(nums2)
        minPrefix1 = [nums1[0]] * len(nums1)
        minPrefix2 = [nums2[0]] * len(nums2)
        for i in range(1, len(nums1)):
            maxPrefix1[i] = max(nums1[i], maxPrefix1[i - 1])
            minPrefix1[i] = min(nums1[i], minPrefix1[i - 1])
        for i in range(1, len(nums2)):
            maxPrefix2[i] = max(nums2[i], maxPrefix2[i - 1])
            minPrefix2[i] = min(nums2[i], minPrefix2[i - 1])

        @lru_cache(None)
        def dp(i, j):
            if i < 0 or j < 0:
                return float("-inf")
            if i == 0:
                return max(nums1[0] * maxPrefix2[j], nums1[0] * minPrefix2[j])
            if j == 0:
                return max(nums2[0] * maxPrefix1[i], nums2[0] * minPrefix1[i])
			
            # if nums1[i] and nums2[j] are not used
            res = dp(i - 1, j - 1)
			
            # if nums1[i] and nums2[j] are paired
            res = max(nums1[i] * nums2[j], res, nums1[i] * nums2[j] + res)
			
            # if either nums1[i] or nums2[j] is used
            res = max(res, dp(i, j - 1), dp(i - 1, j))

            return res
        return dp(len(nums1) - 1, len(nums2) - 1)
