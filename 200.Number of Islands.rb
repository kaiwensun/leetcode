# @param {Character[][]} grid
# @return {Integer}
$DELTA=[1, 0, -1, 0, 1]
def num_islands(grid)
    def dfs(i, j, grid)
        m, n = grid.size, grid[0].size
        if 0 <= i && i < m && 0 <= j && j < n
            if grid[i][j] == '1'
                grid[i][j] = '2'
                (0...4).each do |k|
                    dx, dy = $DELTA[k], $DELTA[k + 1]
                    dfs(i + dx, j + dy, grid)
                end
                return 1
            end
        end
        return 0
    end
    res = 0
    m, n = grid.size, (grid.empty? ? 0 : grid[0].size)
    (0...m).each do |i|
        (0...n).each do |j|
            res += dfs(i, j, grid)
        end
    end
    res
end
