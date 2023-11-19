class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        mn = min(map(len, [s1, s2, s3]))
        for i in range(mn):
            if len(set(s[i] for s in (s1, s2, s3))) != 1:
                break
        else:
            i += 1
        if i == 0:
            return -1
        return sum(map(len, [s1, s2, s3])) - i * 3

