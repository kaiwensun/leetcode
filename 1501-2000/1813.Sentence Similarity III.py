class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        sentence1 = sentence1.split(" ");
        sentence2 = sentence2.split(" ");
        if len(sentence1) > len(sentence2):
            sentence1, sentence2 = sentence2, sentence1
        for i in xrange(len(sentence1)):
            if sentence1[i] != sentence2[i]:
                break
        else:
            i += 1
        for j in xrange(i - len(sentence1), 0):
            if sentence1[j] != sentence2[j]:
                return False
        return True

