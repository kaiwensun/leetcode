"""
There is a proof by enumerating '????' cases that no contenious sequence longer than or equal to length 4 can be created. So don't worry about carry bit
https://leetcode.com/discuss/6762/how-to-proof-the-count-is-always-less-than-10
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        original_lst = [1]
        i=0
        lst=[]
        for x in xrange(n-1):
            while i<len(original_lst):
                token = original_lst[i]
                j=i+1
                while j<len(original_lst) and original_lst[j]==token:
                    j=j+1
                lst.append(j-i)
                lst.append(token)
                i=j
            original_lst = lst
            i=0
            lst=[]
        return "".join(map(lambda c:str(c),original_lst))

