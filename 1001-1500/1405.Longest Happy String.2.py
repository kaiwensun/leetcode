class Solution(object):
    def longestDiverseString(self, a, b, c, a_chr="a", b_chr="b", c_chr="c"):
        if not (a <= b <= c):
            data = sorted([(a, a_chr), (b, b_chr), (c, c_chr)])
            return self.longestDiverseString(data[0][0], data[1][0], data[2][0], data[0][1], data[1][1], data[2][1])
        if b == 0:
            return c_chr * min(2, c)
        if b == c:
            return c_chr + b_chr + self.longestDiverseString(a, b - 1, c - 1, a_chr, b_chr, c_chr)
        return c_chr * 2 + b_chr + self.longestDiverseString(a, b - 1, c - 2, a_chr, b_chr, c_chr)
