class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def get_digit(num, shift):
            return num // (10 ** shift) % 10
        def set_digit(num, d, shift):
            return num + (d - get_digit(num, shift)) * 10 ** shift
        size = len(str(N))
        for i in xrange(size - 1, -1, -1):
            if i != size - 1 and get_digit(N, i) < get_digit(N, i + 1):
                N = N // 10 ** (i + 1) * 10 ** (i + 1) - 1
                for j in xrange(i + 1, size):
                    if get_digit(N, j) < get_digit(N, j + 1):
                        N = set_digit(N, 9, j)
                        N = set_digit(N, get_digit(N, j + 1) - 1, j + 1)
                break
        return N

