# @param {Integer[][]} grid
# @return {Integer}

DELTA = [1, 0, -1, 0, 1].freeze
def island_perimeter(grid)
    for i in 0...grid.size
        for j in 0...grid[i].size
            res = dfs(grid, i, j)
            return res if res.nonzero?
        end
    end
end

def dfs(grid, i, j)
    res = 0
    if is_land(grid, i, j) && grid[i][j] == 1
        grid[i][j] = 2
        res = count_edges(grid, i, j)
        for k in 0...4
            res += dfs(grid, i + DELTA[k], j + DELTA[k + 1])
        end
    end
    res
end

def is_land(grid, i, j)
    0 <= i && i < grid.size && 0 <= j && j < grid[0].size && grid[i][j] != 0
end

def count_edges(grid, i, j)
    res = 0
    for k in 0...4
        res += 1 if !is_land(grid, i + DELTA[k], j + DELTA[k + 1])
    end
    res
end
