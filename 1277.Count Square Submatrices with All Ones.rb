# @param {Integer[][]} matrix
# @return {Integer}
def count_squares(matrix)
    res = 0
    for i in 0...matrix.size
        for j in 0...matrix[i].size
            matrix[i][j] = [matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]].min + 1 if i != 0 && j != 0 && matrix[i][j] == 1
            res += matrix[i][j]
        end
    end
    res
end
