class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        MOD = 10 ** 9 + 7

        def add_to_rolling_sum_right(sm, c, old_length):
            return (sm * 26 + (ord(c) - ord('a'))) % MOD

        def add_to_rolling_sum_left(sm, c, old_length):
            return ((ord(c) - ord('a')) * pow(26, old_length, MOD) + sm) % MOD

        def mergeTwo(m, n):
            if len(m) > len(n):
                m, n = n, m
            yield m + n
            rolling_m = rolling_n = 0
            for i in range(len(m) - 1):
                rolling_m = add_to_rolling_sum_left(rolling_m, m[-i - 1], i)
                rolling_n = add_to_rolling_sum_right(rolling_n, n[i], i)
                if rolling_m == rolling_n:
                    if m[-i-1:] == n[:i + 1]:
                        yield m + n[i + 1:]
            if m in n:
                yield n
            yield n + m
            rolling_m = rolling_n = 0
            for i in range(len(m) - 1):
                rolling_m = add_to_rolling_sum_right(rolling_m, m[i], i)
                rolling_n = add_to_rolling_sum_left(rolling_n, n[-i - 1], i)
                if rolling_m == rolling_n:
                    if n[-i-1:] == m[:i+1]:
                        yield n[:-i-1] + m
        res = a + b + c
        for [x, y, z] in [a, b, c], [a, c, b]:
            for two in mergeTwo(x, y):
                for three in mergeTwo(two, z):
                    if len(three) < len(res):
                        res = three
                    elif len(three) == len(res) and three < res:
                        res = three
        return res

