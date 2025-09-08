class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1

        # Count 0 as a palindromic
        res = 1

        # Set highest bit to 1 for those shorter than length
        length = n.bit_length()
        for i in range(1, length):
            res += 1 << (i - 1) // 2

        # Set highest bit to 1 for those having same length as n.
        # A. If a mid bit is 1, then when we set it to 0 we freely set the rest. (The for loop)
        # B. If a mid bit is 1, then when we set it to 1 we have to set its palindromic partner to 1. (The while loop)
        for i in range(length - 2, length // 2 - 1, -1):
            if (1 << i) & n:
                res += 1 << (i - length // 2)
        s = list(bin(n)[2:])
        l, r = 0, len(s) - 1
        while l < r:
            s[r] = s[l]
            l += 1
            r -= 1
        pal = int("".join(s), 2)
        if pal <= n:
            res += 1
        return res

