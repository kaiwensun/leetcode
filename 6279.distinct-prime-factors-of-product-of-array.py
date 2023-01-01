PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            for prime in PRIMES:
                if prime > num:
                    break
                while num % prime == 0:
                    num //= prime
                    seen.add(prime)
            if num != 1:
                seen.add(num)
        return len(seen)

