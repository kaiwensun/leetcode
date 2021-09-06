from collections import Counter
from functools import cache

MOD = 10 ** 9 + 7
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
INVALID = set()
num_to_prime_bitmap = [0] * 31
for i, prime in enumerate(PRIMES):
    for num in range(prime, len(num_to_prime_bitmap), prime):
        if num % (prime * prime):
            num_to_prime_bitmap[num] |= 1 << i
        else:
            INVALID.add(num)

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for num in list(counter.keys()):
            if num in INVALID:
                del counter[num]
        counter_items = list(counter.items())
        cnt_of_1 = pow(2, counter[1], MOD) - 1

        @cache
        def dp(i, used_primes_bitmap):
            if i == len(counter):
                return 1 if used_primes_bitmap else 0
            num, cnt = counter_items[i]
            prime_bitmap = num_to_prime_bitmap[num]
            res = dp(i + 1, used_primes_bitmap)
            if prime_bitmap & used_primes_bitmap == 0:
                res += dp(i + 1, prime_bitmap | used_primes_bitmap) * (cnt_of_1 if num == 1 else cnt)
                res %= MOD
            return res
        return dp(0, 0)

