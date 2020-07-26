class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        def makeFib(first_str, second_str):
            prefix = first_str + second_str
            if len(prefix) >= len(S): # or not S.startswith(prefix):
                return []
            first, second = int(first_str), int(second_str)
            res = [first, second]
            i = len(prefix)
            while i != len(S):
                first, second = second, first + second
                if second >= 1<<31:
                    return []
                prefix = str(second)
                if S[i:i + len(prefix)] != prefix:
                    return []
                res.append(second)
                i += len(prefix)
            return res
        S1 = "0" if S[0] == "0" else S
        for i in xrange(1, min(10, len(S1)) + 1):
            for j in xrange(i + 1, min(i + 10, len(S)) + 1):
                res = makeFib(S1[:i], S[i:j])
                if res:
                    return res
        return []
