from sortedcontainers import SortedList

# (nums1[i] - nums2[i]) -  (nums1[j] - nums2[j]) <= diff
# d[i] <= diff + d[j]

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        sl = SortedList()
        res = 0
        for d in map(lambda num: num[0] - num[1], zip(nums1, nums2)):
            res += sl.bisect_right(diff + d)
            sl.add(d)
        return res

