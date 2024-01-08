from functools import cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        arr = list(map(lambda c: 1 << (ord(c) - ord('a')), s))
        unique = (1 << 26) - 1
        for a in arr:
            unique &= ~a
        def all_available_bits(bits, bit, can_change):
            yield bit, False
            if can_change:
                if unique:
                    yield unique, True
                else:
                    mask = 1
                    for _ in range(26):
                        if not (mask & bits):
                            yield mask, True
                        mask <<= 1
        @cache
        def dp(i, bits, size, can_change):
            if i == len(arr):
                return 0
            res = 0
            bit = arr[i]
            for bit, changed in all_available_bits(bits, bit, can_change):
                new_size = size if bit & bits else size + 1
                new_bits = bit | bits
                if new_size > k:
                    res = max(res, 1 + dp(i + 1, bit, 1, can_change and not changed))
                else:
                    res = max(res, dp(i + 1, new_bits, new_size, can_change and not changed))
            return res
        return 1 + dp(0, 0, 0, True)

