MOD = (10 ** 9 + 7) * (10 ** 9 + 9)

class Solution:

    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        def hashset(path, length, prevset):
            res = set()
            high_base = 1
            h = 0
            for i, num in enumerate(path):
                h = (h * base + num) % MOD
                if i < length:
                    high_base = (high_base * base) % MOD
                else:
                    h = (h - path[i - length] * high_base) % MOD
                if i >= length - 1 and (prevset is None or h in prevset):
                    res.add(h)
            return res
        
        def test(length):
            res = None
            for path in paths:
                res = hashset(path, length, res)
                if not res:
                    return False
            return True
        
        base = max(map(max, paths))
        l, r = 1, max(map(len, paths)) + 1
        while l < r:
            mid = (l + r) // 2
            if test(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1

