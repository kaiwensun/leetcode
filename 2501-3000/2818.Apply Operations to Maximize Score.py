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

PRIMES = sieve_of_sundaram(10 ** 5)
PRIME_SCORES = [0] * (10 ** 5 + 1)
for prime in PRIMES:
    prime_multi = prime
    while prime_multi < len(PRIME_SCORES):
        PRIME_SCORES[prime_multi] += 1
        prime_multi += prime

MOD = 10 ** 9 + 7

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left_sizes = []
        stack = [[-1, float("inf")]]  # [[index, ps], ...]
        for i, num in enumerate(nums):
            ps = PRIME_SCORES[num]
            while stack[-1][1] < ps:
                stack.pop()
            left_sizes.append(i - stack[-1][0])
            stack.append([i, ps])

        right_sizes = [None] * len(nums)
        stack = [[len(nums), float("inf")]]  # [[index, ps], ...]
        for i, num in reversed(list(enumerate(nums))):
            ps = PRIME_SCORES[num]
            while stack[-1][1] <= ps:
                stack.pop()
            right_sizes[i] = stack[-1][0] - i
            stack.append([i, ps])

        res = 1
        for i, num in sorted(enumerate(nums), key=lambda p: -p[1]):
            ps = PRIME_SCORES[num]
            available_ops = min(k, left_sizes[i] * right_sizes[i])
            res *= pow(num, available_ops, MOD)
            res %= MOD
            k -= available_ops
            if k == 0:
                break
        return res

