import functools
@functools.lru_cache(None)
def power(x):
    if x == 1:
        return 0
    if x % 2:
        return power(x * 3 + 1) + 1
    else:
        return power(x / 2) + 1
  
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        return sorted(range(lo, hi + 1), key=power)[k - 1]
