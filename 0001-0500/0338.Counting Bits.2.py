class Solution(object):
    bit_map = None
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if self.bit_map is None:
            self.bit_map = {
                (1 << i) - 1: i for i in xrange(1, 30)
            }
        rval = [0] * (num + 1)
        for n in xrange(1, num + 1):
            if n - 1 & 1:
                cnt_of_ones = (n ^ (n - 1)) >> 1
                rval[n] = rval[n - 1] - self.bit_map[cnt_of_ones] + 1
            else:
                rval[n] = rval[n - 1] + 1
        return rval
