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

PRIMES = sieve_of_sundaram(10 ** 5 + 3)

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        prime_idx = 0
        sum_a = sum_b = 0
        for i, num in enumerate(nums):
            if i == PRIMES[prime_idx]:
                prime_idx += 1
                sum_a += num
            else:
                sum_b += num
        return abs(sum_a - sum_b)

