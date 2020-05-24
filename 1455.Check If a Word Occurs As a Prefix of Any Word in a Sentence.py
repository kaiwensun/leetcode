class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        for index, word in enumerate(sentence.split(" ")):
            if word.startswith(searchWord):
                return index + 1
        return -1
