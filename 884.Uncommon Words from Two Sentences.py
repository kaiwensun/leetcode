from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        cntA = Counter(A.split(" "))
        cntB = Counter(B.split(" "))
        return [word for word in set(cntA.keys()) ^ set(cntB.keys()) if cntA[word] + cntB[word] == 1]


#    def uncommonFromSentences(self, A, B):
#        c = collections.Counter((A + " " + B).split())
#        return [w for w in c if c[w] == 1]
