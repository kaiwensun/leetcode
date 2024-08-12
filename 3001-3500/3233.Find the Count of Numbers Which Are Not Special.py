import math, bisect

def sieve_of_sundaram(mx):
    if mx < 2:
        return []
    mx_idx = (mx - 1) // 2
    is_prime_idx = [True] * (mx_idx + 1)
    for i in range(1, len(is_prime_idx)):
        if 2 * i * i + i + i > mx_idx:
            break
        for j in range(i, len(is_prime_idx)):
            if 2 * i * j + i + j > mx_idx:
                break
            else:
                is_prime_idx[2 * i * j + i + j] = False
    return [2] + [2 * i + 1 for i, is_prime in enumerate(is_prime_idx) if is_prime and i > 0]

PRIMES_SQR = [num * num for num in sieve_of_sundaram(math.isqrt(10 ** 9) + 1)]


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def count_non_special_nums_smaller_than(num):
            # num is exclusive
            return num - bisect.bisect_left(PRIMES_SQR, num)
        return count_non_special_nums_smaller_than(r + 1) - count_non_special_nums_smaller_than(l)

