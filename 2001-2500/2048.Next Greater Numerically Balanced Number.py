from collections import Counter
import bisect

def is_balance(n):
    cnt = Counter(str(n))
    for d, c in cnt.items():
        if int(d) != c:
            return False
    return True

cache = []

for n in range(10 ** 7):
    if is_balance(n):
        cache.append(n)
        if n > 10 ** 6:
            break

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        return cache[bisect.bisect_right(cache, n)]

