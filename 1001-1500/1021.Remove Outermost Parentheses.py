class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        cnt = 0
        rval = []
        for c in S:
            if c == '(':
                cnt += 1
                if cnt != 1:
                    rval.append('(')
            else:
                cnt -= 1
                if cnt != 0:
                    rval.append(')')
        return ''.join(rval)

