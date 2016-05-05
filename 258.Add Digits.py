"""
Result:
  1101 / 1101 test cases passed.
  Status: Accepted
  Runtime: 62 ms
  Your runtime beats 47.00% of pythonsubmissions.
Date:
  5/5/2016
Idea:
  digital root: https://en.wikipedia.org/wiki/Digital_root
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 0 if num==0 else 9 if num%9==0 else num%9
