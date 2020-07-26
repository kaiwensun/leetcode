class Solution(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        s = hex(int(num)).replace("0", "O").replace("1", "I")[2:].upper()
        return "ERROR" if set("23456789") & set(s) else s
