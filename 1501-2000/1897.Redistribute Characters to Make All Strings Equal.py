from collections import Counter

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        return all(value % len(words) == 0 for value in sum(map(Counter, words), Counter()).values())

