import bisect

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibs = [1, 1]
        while fibs[-1] <= k:
            fibs.append(fibs[-1] + fibs[-2])
        index = len(fibs)
        res = 0
        while k:
            index = bisect.bisect(fibs, k, hi=index) - 1
            k -= fibs[index]
            res += 1
        return res
