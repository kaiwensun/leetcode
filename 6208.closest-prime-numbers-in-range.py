import math
import bisect

MAX = 10 ** 6;

PRIMES = [2];

# Sieve of Sundaram
def sieve():
    n_new = 10 ** 3
    marked = [False] * (MAX // 2 + 500)
    for i in range(1, n_new // 2 + 1):
        for j in range(2 * i * (i + 1), MAX // 2 + 1, 2 * i + 1):
            marked[j] = True
    for i in range(1, MAX // 2 + 1):
        if (marked[i] == 0):
            PRIMES.append(2 * i + 1)

sieve()

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        l = bisect.bisect_left(PRIMES, left)
        diff = float("inf")
        res_ind = -1
        for i in range(l, len(PRIMES) - 1):
            if PRIMES[i + 1] > right:
                break
            new_diff = PRIMES[i + 1] - PRIMES[i]
            if new_diff < diff:
                diff = new_diff
                res_ind = i

        if res_ind == -1:
            return [-1, -1]
        return [PRIMES[res_ind], PRIMES[res_ind + 1]]

