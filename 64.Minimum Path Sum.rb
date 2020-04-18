# @param {Integer[][]} grid
# @return {Integer}
def min_path_sum(grid)
    dp = [1.0/0.0] * (grid[0].size + 1)
    dp[1] = 0
    grid.each do |row|
        new_dp = [1.0/0.0] * (grid[0].size + 1)
        (1..grid[0].size).each { |i|  new_dp[i] = [dp[i], new_dp[i - 1]].min + row[i - 1] }
        dp = new_dp
    end
    dp[-1]
end
