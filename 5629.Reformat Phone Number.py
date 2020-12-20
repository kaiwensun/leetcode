class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        number = number.replace(" ", "").replace("-", "")
        res = []
        for i in xrange(0, len(number), 3):
            res.append(number[i:i+3])
        if len(res) >= 2 and len(res[-1]) == 1:
            a = res.pop()
            b = res.pop() + a
            res.append(b[:2] + "-" + b[2:])
        return "-".join(res)

