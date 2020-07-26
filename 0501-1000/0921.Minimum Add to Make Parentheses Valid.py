class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        counter = 0
        result = 0
        for s in S:
            if s == '(':
                counter += 1
            else:
                if counter == 0:
                    result += 1
                else:
                    counter -= 1
        return result + counter
