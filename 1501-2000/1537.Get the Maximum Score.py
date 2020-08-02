class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.append(0)
        nums2.append(0)
        arrays = [nums1, nums2]
        commons = set(nums1) & set(nums2)
        diffs = [[], []]
        for array_index, nums in enumerate([nums1, nums2]):
            sm = 0
            for num in nums:
                sm += num
                if num in commons:
                    diffs[array_index].append(sm)
                    sm = 0
        
        return sum(max(diffs[0][i], diffs[1][i]) for i in range(len(commons))) % (10 ** 9 + 7)

