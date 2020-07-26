class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        self.mapping = {}
        lines = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
        for i, line in enumerate(lines):
             for c in line:
                    self.mapping[c] = i
        return filter(self.isOneLineWord, words)
        
    def isOneLineWord(self, word):
        inLine = [False, False, False]
        for c in word:
            inLine[self.mapping[c]] = True
        return len(filter(bool, inLine)) <= 1
