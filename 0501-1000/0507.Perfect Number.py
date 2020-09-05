class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        root = int(math.sqrt(num)) + 1
        s = 0
        for i in xrange(1, root):
            if not num % i:
                s += i + num / i
        return num != 1 and s == num * 2
