import collections
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        c = collections.Counter(text)
        #balloon
        return min(c['b'], c['a'], c['l'] / 2, c['o'] / 2, c['n'])
