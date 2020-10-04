from functools import lru_cache

class Solution:
    @lru_cache(None)
    def minimumOneBitOperations(self, n: int, cur=0) -> int:
        def getHighest(n):
            for shift in (1, 2, 4, 8, 16):
                n |= n >> shift
            return (n + 1) >> 1
        
        def isOneBit(n):
            # suppose n != 0
            return n & (n - 1) == 0

        highest = getHighest(n)
        if cur == 0:
            if n <= 1:
                return n
            highestTwo = (highest | (highest >> 1)) & n
            if isOneBit(highestTwo):
                # n == 10xxxxx
                return self.minimumOneBitOperations(highest >> 1, 0) + 1 + self.minimumOneBitOperations(n - highest, highest >> 1)
            else:
                # n == 11xxxxx
                return self.minimumOneBitOperations(highest >> 1) + 1 + self.minimumOneBitOperations(n - highestTwo)
        else:
            # isOneBit(cur) must be true here
            if cur == highest:
                return self.minimumOneBitOperations(n - cur, 0)
            elif cur > highest:
                return self.minimumOneBitOperations(cur >> 1) + 1 + self.minimumOneBitOperations(n, cur >> 1)
            else:
                assert(False)

