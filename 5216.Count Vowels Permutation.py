class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        def calcA():
            return lastRound[1]
        def calcE():
            return (lastRound[0] + lastRound[2]) % MOD
        def calcI():
            return (lastRound[0] + lastRound[1] + lastRound[3] + lastRound[4]) % MOD
        def calcO():
            return (lastRound[2] + lastRound[4]) % MOD
        def calcU():
            return lastRound[0]
        
        funcs = [calcA, calcE, calcI, calcO, calcU]
        dp = [1] * 5
        for i in xrange(n - 1):
            lastRound = dp
            dp = [0] * 5
            for vowel in xrange(5):
                dp[vowel] = funcs[vowel]()
        return sum(dp) % MOD
