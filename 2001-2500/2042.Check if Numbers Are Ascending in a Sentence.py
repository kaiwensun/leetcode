class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num = -1
        for token in s.split():
            if '0' <= token[0] <= '9':
                if num >= int(token):
                    return False
                num = int(token)
        return True

