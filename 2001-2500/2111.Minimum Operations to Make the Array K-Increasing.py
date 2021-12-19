import bisect

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        res = 0
        for start in range(k):
            inc = [-1]
            for i in range(start, len(arr), k):
                num = arr[i]
                j = bisect.bisect_right(inc, num)
                if (j == len(inc)):
                    inc.append(num)
                else:
                    inc[j] = num
            res += len(inc) - 1
        return len(arr) - res

