import string
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # (look at word[:i + 1], the last letter no bigger than j) => the min number of deletion needed
        ordered = [False] * (len(A) - 1)
        rval = 0
        for i in xrange(len(A[0])): # word length
            col_ordered = [False] * (len(A) - 1)
            has_conflict = False
            for j in xrange(len(A) - 1):    # cnt of words
                if ordered[j]:
                    continue
                word1 = A[j]
                word2 = A[j + 1]
                if word1[i] < word2[i]:
                    col_ordered[j] = True
                if word1[i] > word2[i]:
                    has_conflict = True
            if not has_conflict:
                for i in xrange(len(ordered)):
                    ordered[i] = ordered[i] or col_ordered[i]
            else:
                rval += 1
        return rval
