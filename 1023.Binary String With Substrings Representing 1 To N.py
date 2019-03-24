class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        seen = set()
        cnt = 0
        for i in xrange(len(S)):
            if S[i] == '0':
                continue
            for j in xrange(i + 1, len(S) + 1):
                num = int(S[i:j], 2)
                if num > N:
                    break
                if num not in seen:
                    seen.add(num)
                    cnt += 1
                    if cnt == N:
                        return True
        return False
