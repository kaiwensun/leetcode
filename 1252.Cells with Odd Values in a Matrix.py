class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        rows = set()
        cols = set()
        for r, c in indices:
            rows ^= {r}
            cols ^= {c}
        print(rows, cols)
        rl = len(rows)
        cl = len(cols)
        return rl * m + cl * n - 2 * rl * cl
