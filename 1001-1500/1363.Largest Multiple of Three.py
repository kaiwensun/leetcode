class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        n = len(digits)
        digits = sorted(digits, reverse=True)
        res = [0]
        if digits[0] != 0:
            s = sum(digits)
            res = digits
            if s % 3 == 0:
                pass
            elif s % 3 == 1:
                for i in xrange(n - 1, -1, -1):
                    if res[i] % 3 == 1:
                        res.pop(i)
                        break
                else:
                    cnt = 0
                    for i in xrange(n - 1, -1, -1):
                        if res[i] % 3 == 2:
                            res.pop(i)
                            cnt += 1
                        if cnt == 2:
                            break
                    else:
                        res = []
            elif s % 3 == 2:
                for i in xrange(n - 1, -1, -1):
                    if res[i] % 3 == 2:
                        res.pop(i)
                        break
                else:
                    cnt = 0
                    for i in xrange(n - 1, -1, -1):
                        if res[i] % 3 == 1:
                            res.pop(i)
                            cnt += 1
                        if cnt == 2:
                            break
                    else:
                        res = []
        return "".join(map(str, res))
                
        
