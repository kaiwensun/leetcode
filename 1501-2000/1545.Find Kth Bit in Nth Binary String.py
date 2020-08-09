from functools import lru_cache

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        @lru_cache(None)
        def getSize(n):
            if n == 1:
                return 1
            else:
                return getSize(n - 1) * 2 + 1
        def search(n, k):
            size = getSize(n)
            mid = size // 2 + 1
            if k == 1:
                res = 0
            elif k < mid:
                res = search(n - 1, k)
            elif k == mid:
                res = 1
            else:
                res = 1 - search(n - 1, size - k + 1)
            return res
        return str(search(n, k))

