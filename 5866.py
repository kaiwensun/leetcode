IS_PRIME = [True] * (10 ** 5 + 1)
for base in range(2, len(IS_PRIME)):
    for num in range(base * 2, len(IS_PRIME), base):
        IS_PRIME[num] = False

PRIMES = [i for i in range(2, len(IS_PRIME)) if IS_PRIME[i]]

class Solution:

    def gcdSort(self, nums: List[int]) -> bool:

        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]
        def union(x, y):
            rx = find(x)
            ry = find(y)
            data[rx] = ry

        seen = set(nums)
        MAX = max(nums)
        data = {num:num for num in seen}

        for prime in PRIMES:
            if prime > MAX:
                break
            data.setdefault(prime, prime)
            for acc in range(prime, MAX + 1, prime):
                if acc in seen:
                    union(acc, prime)

        targets = sorted(nums)
        for i in range(len(nums)):
            if find(nums[i]) != find(targets[i]):
                return False
        return True

