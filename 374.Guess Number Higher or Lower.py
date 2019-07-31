# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n + 1
        while start != end:
            mid = start + (end - start) / 2
            res = guess(mid)
            if res == 0:
                return mid
            if res > 0:
                start = mid + 1
            else:
                end = mid
        return start
