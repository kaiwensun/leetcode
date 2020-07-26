class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self._n = n
        self._buf = [None] * n + nums
        for i in xrange(n - 1, 0, -1):
            self._buf[i] = self._buf[i * 2] + self._buf[i * 2 + 1]
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        i = self._n + i
        self._buf[i] = val
        while i > 1:
            i /= 2
            self._buf[i] = self._buf[i * 2] + self._buf[i * 2 + 1]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        i += self._n
        j += self._n + 1
        res = 0
        while i < j:
            if i % 2:
                res += self._buf[i]
                i += 1
            if j % 2:
                j -= 1
                res += self._buf[j]
            i /= 2
            j /= 2
        return res

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
