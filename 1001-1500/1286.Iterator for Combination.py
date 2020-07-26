# This solution is cheating

from itertools import combinations
class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.it = combinations(characters, combinationLength)
        self.buffer = "".join(next(self.it)) if characters else None
        

    def next(self):
        """
        :rtype: str
        """
        res = self.buffer
        try:
            self.buffer = "".join(next(self.it))
        except:
            self.buffer = None
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.buffer is not None
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
