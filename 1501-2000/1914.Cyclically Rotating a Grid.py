class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(grid), len(grid[0])

        def start(i):
            return i + i * 1j

        def height(i):
            return m - 2 * i - 1

        def width(i):
            return (n - 2 * i) - 1

        def loop_size(i):
            return (height(i) + width(i)) * 2

        def index_in_loop_to_point(i, index):
            point = start(i)
            direct = 1
            for size in height(i), width(i), height(i), width(i):
                point += direct * min(size, index)
                index -= size
                direct *= 1j
                if index <= 0:
                    break
            return point

        res = [[None] * n for _ in range(m)]
        for i in range(min(m, n) // 2):
            src = start(i)
            direct = 1
            lsize = loop_size(i)
            tar_index = k % lsize
            for size in height(i), width(i), height(i), width(i):
                for _ in range(size):
                    tar = index_in_loop_to_point(i, tar_index)
                    res[int(tar.real)][int(tar.imag)] = grid[int(src.real)][int(src.imag)]
                    src += direct
                    tar_index += 1
                    tar_index %= lsize
                direct *= 1j
        return res


