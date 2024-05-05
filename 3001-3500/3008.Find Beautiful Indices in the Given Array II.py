MOD = 10 ** 9 + 7

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        @cache
        def rolling_sum(i, length):
            if i == 0:
                sm = 0
                for j in range(length):
                    sm *= 26
                    sm += ord(s[j]) - ord('a')
                    sm %= MOD
                return sm
            base = rolling_sum(i - 1, length) * 26
            base -= (ord(s[i - 1]) - ord('a')) * pow(26, length, MOD)
            base += (ord(s[i + length - 1]) - ord('a'))
            return base % MOD
        def find_index(x):
            sm = 0
            for j in range(len(x)):
                sm *= 26
                sm += ord(x[j]) - ord('a')
                sm %= MOD
            sums = [rolling_sum(i, len(x)) for i in range(len(s) - len(x) + 1)]
            return [i for i, e in enumerate(sums) if sm == e]
        
            
        a_index = find_index(a)
        b_index = find_index(b)
        b_index.append(float("inf"))
        res = []
        for i in a_index:
            t = bisect_right(b_index, i)
            for tt in t - 1, t,:
                if abs(b_index[tt] - i) <= k:
                    res.append(i)
                    break
        return res

