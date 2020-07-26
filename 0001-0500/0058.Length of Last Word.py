class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        while i<len(s):
            if s[-i-1]!=' ':
                break
            i+=1
        tail = i
        while i<len(s):
            if s[-i-1]==' ':
                return i-tail
            i+=1
        return i-tail
        

