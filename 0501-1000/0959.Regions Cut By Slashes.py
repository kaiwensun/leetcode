class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        U, R, D, L = 0b1, 0b10, 0b100, 0b1000
        M, N = len(grid), len(grid[0])
        visited = [[0] * N for _ in xrange(M)]

        def get_piece(i, j, posi):
            if grid[i][j] == "/":
                return (L | U) if posi & (L | U) else (R | D)
            elif grid[i][j] == "\\":
                return (R | U) if posi & (R | U) else (L | D)
            else:
                return U | R | D | L
        
        def get_opposite_posi(posi):
            return ((posi << 2) | (posi >> 2)) & (0xF)
        
        def dfs(i, j, posi, top=False):
            if not (0 <= i < M and 0 <= j < N):
                return 0
            piece = get_piece(i, j, posi)
            if visited[i][j] & piece:
                return 0
            visited[i][j] |= piece
            for dx, dy, dposi in ((-1, 0, U), (0, 1, R), (1, 0, D), (0, -1, L)):
                if dposi & piece:
                    dfs(i + dx, j + dy, get_opposite_posi(dposi))
            return 1

        return sum(dfs(i, j, piece) for i in xrange(M) for j in xrange(N) for piece in [U, D])

