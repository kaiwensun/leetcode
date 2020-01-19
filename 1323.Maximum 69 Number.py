class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        for i, n in enumerate(num):
            if n == "6":
                num[i] = "9"
                break
        return int("".join(num))
