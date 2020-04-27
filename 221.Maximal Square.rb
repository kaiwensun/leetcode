# @param {Character[][]} matrix
# @return {Integer}
def maximal_square(matrix)
    res = 0
    if !matrix.empty?
        size = matrix[0].size
        dp = [0] * (size + 1)
        for i in (0...matrix.size)
            topleft = 0
            for j in (0...matrix[i].size)
                top = dp[j + 1]
                left = dp[j]
                if matrix[i][j] == "0"
                    dp[j + 1] = 0
                else
                    dp[j + 1] = 1 + [left, topleft, top].min
                end
                res = [dp[j + 1], res].max
                topleft = top
            end
        end
    end
    res * res
end
