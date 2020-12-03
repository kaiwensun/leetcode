class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = []
        is_prime = [True] * (n)
        for x in xrange(2, n):
            if is_prime[x]:
                primes.append(x)
            for prime in primes:
                if x * prime >= n:
                    break
                is_prime[x * prime] = False
                if x % prime == 0:
                    break
        return len(primes)

