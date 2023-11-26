MOD = 10 ** 9 +7

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        if n == 0:
            return (a * b) % MOD
        const_a, const_b = a, b
        diff_bits = a ^ b
        res = float("-inf")
        for prefer_a in True, False:
            a, b = const_a, const_b
            i = 0
            x = 0
            mask = (1 << n) - 1
            pulse = 1 << (n - 1)
            a &= ~mask
            b &= ~mask
            while mask:
                if diff_bits & pulse:
                    if a < b:
                        a |= pulse
                    elif a > b:
                        b |= pulse
                    else:
                        if prefer_a:
                            a |= pulse
                        else:
                            b |= pulse
                        prefer_a = not prefer_a
                else:
                    a |= pulse
                    b |= pulse
                mask >>= 1
                pulse >>= 1
            res = max(res, a * b)
        return res %MOD

