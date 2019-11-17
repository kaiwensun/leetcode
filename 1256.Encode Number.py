class Solution(object):
    def encode(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return ""
        base = 0
        bit_length = 0
        while base < num:
            bit_length += 1
            base += 1 << bit_length
        return ("{:0" + str(bit_length) + "b}").format(num - (base - (1 << bit_length)) - 1)
        
        
"""
Another solution - https://leetcode.com/problems/encode-number/discuss/430488/JavaC%2B%2BPython-Binary-of-n-%2B-1

    def encode(self, n):
        return bin(n + 1)[3:]
"""
