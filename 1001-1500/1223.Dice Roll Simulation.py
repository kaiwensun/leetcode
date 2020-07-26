import functools
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ALL = -MOD
        @functools.lru_cache(None)
        def count(i, outcome, consecutive):
            res = 0
            if consecutive == 0:
                for prevout in range(6):
                    if prevout == outcome:
                        continue
                    res += count(i, prevout, ALL)
                    res %= MOD
                return res
            if consecutive - i == 1 or (i == 0 and consecutive == ALL):
                return 1
            if ALL != consecutive < 0:
                return 0
            if i <= 0 or consecutive > rollMax[outcome]:
                return 0
            if consecutive == ALL:
                for j in range(1, rollMax[outcome] + 1):
                    res += count(i, outcome, j)
                    res %= MOD
                return res
            diff = min(i, consecutive)
            return count(i - diff, outcome, consecutive - diff)

        return sum(count(n - 1, outcome,ALL) for outcome in range(6)) % MOD
