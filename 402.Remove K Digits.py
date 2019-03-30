class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        num = list(num)
        i = 0
        while k and i < len(num):
            if i == len(num) - 1 or num[i] > num[i + 1]:
                num.pop(i)
                k -= 1
                i = max(0, i - 1)
            else:
                i += 1
        while num and num[0] == '0':
            num.pop(0)
        if not num:
            return '0'
        return ''.join(num)
