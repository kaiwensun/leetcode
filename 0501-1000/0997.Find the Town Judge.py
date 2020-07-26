class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        s = set(range(1, N + 1))
        for tr in trust:
            s.discard(tr[0])
        if len(s) != 1:
            return -1
        j = s.pop()
        for tr in trust:
            if tr[1] == j:
                s.add(tr[0])
        if len(s) == N - 1:
            return j
        return -1
