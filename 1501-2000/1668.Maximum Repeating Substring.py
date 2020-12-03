class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        for res in xrange(1, len(sequence) + 2):
            if word * res not in sequence:
                return res - 1

