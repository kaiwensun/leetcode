# [Time Limit Exceeded, due to inefficiency of Ruby Hash]
# @param {Integer[][]} grid
# @return {Integer}
def cherry_pickup(grid)
    def search(i, j1, j2, grid, dp)
        return 0 if i >= grid.size || !(0 <= j1 && j1 < grid[0].size) || !(0 <= j2 && j2 < grid[0].size)
        j1, j2 = j2, j1 if j1 > j2
        if !dp.include? [i, j1, j2]
            if j1 == j2
                pick = grid[i][j1]
            else
                pick = grid[i][j1] + grid[i][j2]
            end
            mx = 0
            for next_j1 in (j1 - 1 .. j1 + 1)
                for next_j2 in (j2 - 1 .. j2 + 1)
                    mx = [mx, search(i + 1, next_j1, next_j2, grid, dp)].max
                end
            end
            dp[[i, j1, j2]] = pick + mx
        end
        dp[[i, j1, j2]]
    end
    search(0, 0, grid[0].size - 1, grid, {})
end
