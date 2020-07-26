class MyCounter(collections.Counter):
    def __hash__(self):
        return hash(self.digest())
    def digest(self):
        return tuple(self[c] for c in string.ascii_lowercase)
    def __eq__(self, other):
        return self.digest() == other.digest()

class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return len(set((MyCounter(a[0::2]), MyCounter(a[1::2])) for a in A))
