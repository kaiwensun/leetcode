class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        def b2i(b):
            res = 0
            two = 1
            for n in reversed(b):
                res += two * n
                two *= -2
            return res
        def i2b(n):
            res = []
            while n:
                reminder = (-n) % 2
                res.append(reminder)
                n -= reminder
                n /= (-2)
            if not res:
                return [0]
            res.reverse()
            return res
        s = b2i(arr1) + b2i(arr2)
        return i2b(s)
