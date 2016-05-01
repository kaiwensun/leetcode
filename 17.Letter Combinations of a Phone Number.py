#Idea: mimic digit carry. In what case a digit will carry is determined by the phone number on this digit.
phone = [' ','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        rtn = []
        init_word=[phone[int(x)][0] for x in digits]
        word = init_word
        indicator = [0]*len(digits)
        carry_dig = len(digits)-1
        while carry_dig>=0:
            rtn.append("".join(word))
            carry_dig = len(digits)-1
            indicator[carry_dig]=indicator[carry_dig]+1
            word[carry_dig]=str(unichr(ord(word[carry_dig])+1))
            while indicator[carry_dig]>=len(phone[int(digits[carry_dig])]):
                #fix carry
                if carry_dig<0:
                    return rtn
                indicator[carry_dig]=0
                word[carry_dig]=phone[int(digits[carry_dig])][0]
                carry_dig=carry_dig-1
                indicator[carry_dig]=indicator[carry_dig]+1
                word[carry_dig]=str(unichr(ord(word[carry_dig])+1))
        return rtn
