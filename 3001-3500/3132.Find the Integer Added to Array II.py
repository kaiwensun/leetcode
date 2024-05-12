class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        def test(diff, nums1, nums2):
            iter1, iter2 = iter(nums1), iter(nums2)
            mismatch = 0
            while (num2 := next(iter2, None)) is not None:
                while (num1 := next(iter1, float("inf"))) + diff != num2:
                    mismatch += 1
                    if mismatch > 2:
                        return False
            return True

        nums1.sort()
        nums2.sort()
        res = float("inf")
        for num1 in nums1[:3]:
            diff = nums2[0] - num1
            if test(diff, nums1, nums2):
                res = min(res, diff)
        return res

