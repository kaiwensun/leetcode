class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = range(1, n + 1)
        for i in xrange(len(res)):
            if res[i] % 3 == 0 and res[i] % 5 == 0:
                res[i] = 'FizzBuzz'
            elif res[i] % 3 == 0:
                res[i] = 'Fizz'
            elif res[i] % 5 == 0:
                res[i] = 'Buzz'
            else:
                res[i] = str(res[i])
        return res
