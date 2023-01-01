class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        length = len(str(k))
        res = 0
        start = 0
        while start < len(s):
            if int(s[start : start + length]) <= k:
                start += length
            elif length == 1:
                return -1
            else:
                start += length - 1
            res += 1
        return res

