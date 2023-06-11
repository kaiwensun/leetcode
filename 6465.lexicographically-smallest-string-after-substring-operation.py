class Solution:
    def smallestString(self, s: str) -> str:
        started = False
        s = list(s)
        for i, c in enumerate(s):
            if c == 'a':
                if started:
                    break
            else:
                started = True
                s[i] = chr(ord(c) - 1)
        if not started:
            s[-1] = 'z'
        return ''.join(s)

