# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
import functools
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        LEN = mountain_arr.length()
        @functools.lru_cache(LEN)
        def get(i):
            return mountain_arr.get(i)
        
        def getPeakIndex(start, end):
            while start < end:
                mid = (end - start) // 2 + start
                v = get(mid)
                if get(mid - 1) < v > get(mid + 1):
                    return mid
                if get(mid - 1) < v < get(mid + 1):
                    start = mid + 1
                else:
                    end = mid
        
        def binarySearch(start, end, is_inc):
            while start < end:
                mid = (start + end) // 2
                v = get(mid)
                if v == target:
                    return mid
                if (v < target) == is_inc:
                    start = mid + 1
                else:
                    end = mid
            return -1
        peak_ind = getPeakIndex(0, LEN)
        if get(peak_ind) == target:
            return peak_ind
        res = binarySearch(0, peak_ind, is_inc=True)
        if res != -1:
            return res
        return binarySearch(peak_ind + 1, LEN, is_inc=False)
