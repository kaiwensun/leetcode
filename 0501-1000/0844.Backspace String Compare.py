class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        self.s = len(S) - 1
        self.t = len(T) - 1
        
        def nextS(S):
            if self.s < 0:
                return ''
            c = 0
            while c > 0 or S[self.s] == '#':
                if S[self.s] == '#':
                    c += 1
                else:
                    c -= 1
                self.s -= 1
                if self.s == -1:
                    return ''
            self.s -= 1
            return S[self.s + 1]
        def nextT(T):
            if self.t < 0:
                return ''
            c = 0
            while c > 0 or T[self.t] == '#':
                if T[self.t] == '#':
                    c += 1
                else:
                    c -= 1
                self.t -= 1
                if self.t == -1:
                    return ''
            self.t -= 1
            return T[self.t + 1]
        while self.s >= 0 or self.t >= 0:
            ns = nextS(S)
            nt = nextT(T)
            if ns != nt:
                return False
        return True
