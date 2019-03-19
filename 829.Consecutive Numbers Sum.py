class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        rval = 0
        cnt = 1 # cnt of consecutive positive numbers
        while True:
            rect = N - (cnt + 1) * cnt / 2
            if rect < 0:
                break
            if rect % cnt == 0:
                rval += 1
            cnt += 1
        return rval
