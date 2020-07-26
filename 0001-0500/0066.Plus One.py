class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)-1
        while i>=0:
            if digits[i]!=9:
                break
            digits[i]=0
            i-=1
        if i==-1:
            digits.insert(0,1)
        else:
            digits[i]+=1
        return digits
        

