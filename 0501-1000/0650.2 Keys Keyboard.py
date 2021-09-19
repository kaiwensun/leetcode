N = 1001
IS_PRIMES = [True] * N
for i in range(2, N):
    if IS_PRIMES[i]:
        for j in range(i + i, N, i):
            IS_PRIMES[j] = False

PRIMES = [i for i in range(2, N) if IS_PRIMES[i]]

class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        for prime in PRIMES:
            if n == 1:
                break
            while n != 1 and n % prime == 0:
                res += prime
                n //= prime
        return res

