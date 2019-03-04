from collections import Counter
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        result = Counter(A[0])
        for a in A[1:]:
            counter = Counter(a)
            for key, value in counter.items():
                counter[key] = min(result[key], value)
            result = counter
        rval = []
        for key, value in result.items():
            if value:
                rval.extend([key] * value)
        return rval
            
