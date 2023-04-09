IS_PRIME = [True] * (4 * 10 ** 6 + 1)
IS_PRIME[0] = IS_PRIME[1] = False
sqrt = len(IS_PRIME) // 2 + 1
for base in range(2, sqrt):
    if not IS_PRIME[base]:
        continue
    for num in range(base * 2, sqrt, base):
        IS_PRIME[num] = False

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def prime(num):
            return num if IS_PRIME[num] else 0
        res = 0
        for i in range(len(nums)):
            res = max(res, prime(nums[i][i]), prime(nums[i][len(nums) - 1 - i]))
        return res

