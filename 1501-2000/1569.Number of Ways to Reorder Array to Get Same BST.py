from functools import lru_cache

@lru_cache(None)
def fact(n):
    if n == 0:
        return 1
    return fact(n - 1) * n

def getSlots(ball, box):
    return fact(ball+box-1) // fact(box-1) // fact (ball)

MOD = 10 ** 9 + 7

class Solution(object):
    def numOfWays(self, nums: List[int], is_top=1) -> int:
        def choose_m_from_n(m, n):
            return fact(n) // fact(m) // fact(n - m)
        
        if len(nums) <= 1:
            return 1 - is_top
        root = nums[0]
        left, right = [], []
        for num in nums[1:]:
            if num < root:
                left.append(num)
            else:
                right.append(num)
        slots = getSlots(len(right), (len(left) + 1))
        arrange_left = self.numOfWays(left, 0)
        arrange_right = self.numOfWays(right, 0)
        return (slots * arrange_left * arrange_right - is_top) % MOD

