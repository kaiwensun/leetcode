class Solution(object):
    dp = [0]
    invalid = set('347')
    pair = set('2569')
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if len(self.dp) - 1 >= N:
            return self.dp[N]
        for n in xrange(len(self.dp), N + 1):
            isGood = False
            for c in str(n):
                if c in self.pair:
                    isGood = True
                elif c in self.invalid:
                    self.dp.append(self.dp[-1])
                    break
            else:
                self.dp.append(self.dp[-1] + int(isGood))
        return self.dp[-1]

