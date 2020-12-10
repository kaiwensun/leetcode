import fractions
class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        def genNext(A, B):
            resA = resB = 0
            if resA >= resB:
                resA, resB = resB, resA
            while True:
                if resA == resB:
                    resA += A
                    resB += B
                elif resA < resB:
                    resA += A
                else:
                    resB += B
                yield min(resA, resB)

        MOD = 10 ** 9 + 7
        gcd = fractions.gcd(A, B)
        lcm = A * B // gcd
        loop_size = lcm // A + lcm // B - 1
        loop_cnt = N // loop_size
        res = loop_cnt * lcm
        remain_count = N % loop_size
        remain = 0
        generator = genNext(A, B)
        for _ in xrange(remain_count):
            remain = next(generator)
        return (res + remain) % MOD


