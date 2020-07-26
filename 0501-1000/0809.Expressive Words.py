class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        regex = self.getRegex(S)
        return len(filter(regex.match, words))
        
    def getRegex(self, S):
        i = 0
        exp = ''
        while i <len(S):
            if i + 2 < len(S) and S[i] == S[i + 1] == S[i + 2]:
                j = i + 1
                while j < len(S) and S[j] == S[i]:
                    j += 1
                exp = exp + S[i] + '{1,%s}' % (j - i)
                i = j
            else:
                exp += S[i]
                i += 1
        exp = '^' + exp + '$'
        return re.compile(exp)
