import bisect, collections

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        
        def reverse_bisect(arr, target, lo):
            hi = len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] <= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo - 1

        def next_permutation(num):
            for i in range(len(num) - 2, -1, -1):
                if num[i] < num[i + 1]:
                    j = reverse_bisect(num, num[i], lo=i)
                    num[i], num[j] = num[j], num[i]
                    num[i + 1:] = sorted(num[i + 1:])
                    return num
            assert(False)
        num_frozen = num
        num = list(num)
        for _ in range(k):
            num = next_permutation(num)
        res = 0
        for i in range(len(num)):
            target = num_frozen[i]
            for j in range(i, len(num)):
                if num[j] == target:
                    res += j - i
                    num[i + 1 : j + 1] = num[i:j]
                    break
        return res

