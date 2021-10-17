import bisect

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def binary_search_left(production):
            res = 0
            for i in range(len(nums1)):
                if nums1[i] == 0:
                    res += 0 if production <= 0 else len(nums2)
                else:
                    if nums1[i] < 0:
                        res += len(nums2) - bisect.bisect_right(nums2, production / nums1[i])
                    else:
                        res += bisect.bisect_left(nums2, production / nums1[i])
            return res

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l, r = -10 ** 10, 10 ** 10 + 1
        while l < r:
            mid = (l + r) // 2
            i = binary_search_left(mid)
            if i + 1 <= k:
                l = mid + 1
            else:
                r = mid
        return l - 1

