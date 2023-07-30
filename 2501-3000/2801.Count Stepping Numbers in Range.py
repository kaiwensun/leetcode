from functools import cache

class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10 ** 9 +7
        low = str(int(low) - 1)

        @cache
        def dp(choose_num, i, no_more_than):
            """
            choose_num:   the number determined for the most-significant digit
            i:            the remaining number of digits to consider
            no_more_than: use high or use low as the upper bound of the numbers to count. if None, means do not care about it.
            """
            assert(i != 0)
            if no_more_than is None:
                if i == 1:
                    return 1
                res = dp(choose_num + 1, i - 1, None) if choose_num != 9 else 0
                res += dp(choose_num - 1, i - 1, None) if choose_num != 0 else 0
                return res % MOD
            else:
                no_more_than_num = high if no_more_than == 'high' else low
                nmt_digit = int(no_more_than_num[-i])
                if nmt_digit < choose_num:
                    return 0
                elif nmt_digit == choose_num:
                    if i == 1:
                        return 1
                    res = dp(choose_num + 1, i - 1, no_more_than) if choose_num != 9 else 0
                    res += dp(choose_num - 1, i - 1, no_more_than) if choose_num != 0 else 0
                    return res % MOD
                else: # st_digit > choose_num
                    if i == 1:
                        return 1
                    res = dp(choose_num + 1, i - 1, None) if choose_num != 9 else 0
                    res += dp(choose_num - 1, i - 1, None) if choose_num != 0 else 0
                    return res % MOD

        high_res = low_res = 0

        for length in range(1, len(high) + 1):
            for choose_num in range(1, 10):
                high_res += dp(choose_num, length, 'high' if length == len(high) else None)
                high_res %= MOD

        for length in range(1, len(low) + 1):
            for choose_num in range(1, 10):
                low_res += dp(choose_num, length, 'low' if length == len(low) else None)
                low_res %= MOD

        return (high_res - low_res) % MOD

