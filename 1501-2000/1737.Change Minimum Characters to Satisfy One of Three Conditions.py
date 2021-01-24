import string
class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        total = len(a) + len(b)
        a = Counter(a)
        b = Counter(b)
        res = float('inf')
        for x, y in ((a, b), (b, a)):
            x_total = 0
            y_total = sum(y.values())
            for c in string.ascii_lowercase[:-1]:
                x_total += x[c]
                y_total -= y[c]
                res = min(res, x_total + y_total)
        for c in string.ascii_lowercase:
            res = min(res, total - a[c] - b[c])
        return res

