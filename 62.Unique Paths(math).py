"""
Basic idea:
	There are (m-1)+(n-1) steps from start to final. (m-1) of them are moving down, and (n-1) of them are moving right.
	The number of distinct path is equal to the number of distinct way of "choosing (m-1) from ((m-1)+(n-1)"

61 / 61 test cases passed.
Status: Accepted
Runtime: 36 ms
Your runtime beats 88.43% of python submissions.
"""
from math import factorial as fac
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m>n:
            tmp=m;m=n;n=tmp;
        if m==0:
            return 0
        a=fac(n+m-2)
        b=fac(m-1)
        c=fac(n-1)
        return a/b/c
